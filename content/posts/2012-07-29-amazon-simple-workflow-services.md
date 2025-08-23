Title: Amazon Simple Workflow Services
Date: 2012-07-29 00:00
Slug: 2012/07/29/amazon-simple-workflow-services
Save_as: 2012/07/29/amazon-simple-workflow-services/index.html
URL: 2012/07/29/amazon-simple-workflow-services/
Tags: Amazon, AWS, Ruby
Summary: An introduction to Amazon Simple Workflow Service for coordinating distributed application components. Explains decider and worker roles, task-based workflow execution, reliability features like retries and timeouts, and provides Ruby code examples for registering workflow types and processing tasks.

I’ve been researching [Amazon Simple Workflow Services](http://aws.amazon.com/swf/). This is a product which is like [Simple Queuing Services](http://aws.amazon.com/sqs/) but on steroids. It allows you to develop complex workflows that you’re able to scale out each part of the workflow as you need. There are a number of used cases on their site, one that managed to catch my eye is NASA. They are using Amazon Simple Workflow to process images captured by the Mars Exploration Rovers.

I originally looked into Amazon Simple Workflow sometime ago when it first came out. At the time I was very confused with their API and I didn’t feel that their documentation was complete. Looking into it again for a project at work with different eyes I was able to understand the API a bit more then last time. I still feel that the documentation is a bit lacking along with useful API calls missing. Because of this I feel that there is a steep learning curve and converting an app to use Simple Workflow would take some time.

After my research, I presented my findings to my teammates. I wanted to show them a demo that I could use to point out the different parts of the workflow. For my demo I made a [sandwich maker](https://github.com/amscotti/Simple_workflow_sandwich_maker), this code will allow you to build a sandwich from a web interface and deliver the order to the backend. At this point the decision part of the code which monitors the entire workflow will assign certain task to workers.

In my example I have one worker that can handle all the tasks, if I wanted to scale this out I could increase the number of workers and I would be able to process more tasks. If you wanted to fine-tune this example you could break the code from one worker into multiple workers for a precise task which would allow you to scale individual tasks. This dramatically allows you to scale your application needs and also allows you to configure your system the way you want it to be laid out.

Decision Code,

```ruby
require 'rubygems'
require "aws-sdk"
require "yaml"

#To load the configuration file
CONFIG = YAML.load_file("config.yml") unless defined? CONFIG

#This is for Foreman can properly get the output.
$stdout.sync = true

AWS.config(:access_key_id => CONFIG['access_key_id'], :secret_access_key => CONFIG['secret_access_key'])
swf = AWS::SimpleWorkflow.new
domain = swf.domains[CONFIG['swf_domains']]

#Used to figure out what has happened completed.
def done_task(events)
  ids = []
	task = []
	events.each do |e|
		if e.to_h[:event_type] == 'ActivityTaskCompleted'
			ids << e.to_h[:attributes][:scheduled_event_id]
		elsif e.to_h[:event_type] == 'ActivityTaskScheduled' && ids.include?(e.to_h[:event_id])
			task << e.to_h[:attributes][:activity_type].name
		end
	end
	return task
end

#Used to get the original input sent from the Web server.
def getInput(events)
	events.each do |e|
		if e.to_h[:event_type] == 'WorkflowExecutionStarted'
			return e.to_h[:attributes][:input]
		end
	end
	return ""
end


domain.decision_tasks.poll(CONFIG['swf_task_list']) do |task|
	events_list = task.workflow_execution.events.reverse_order
	done_task_list = done_task(events_list)
	input_json = getInput(events_list)
	begin
		input = JSON.parse(input_json)
	rescue
    	task.cancel_workflow_execution
    	next
  	end

	if !done_task_list.include?("Get-bread")
		orderText = "Starting new order for #{input['name']}, a #{input['fillings'].join(', ')} on #{input['bread']}"
		if input['spread'] != "None"
			orderText += " with #{input['spread']}"
		end
		if input['toasted'] == "true"
			orderText += " toasted"
		end
		puts orderText
		task.schedule_activity_task domain.activity_types['Get-bread', '1'], :input => input_json
	elsif input['spread'] != "None" && done_task_list.include?("Get-bread") && !done_task_list.include?("Add-spread")
		task.schedule_activity_task domain.activity_types['Add-spread', '1'], :input => input_json
	elsif !done_task_list.include?("Add-fillings")
		task.schedule_activity_task domain.activity_types['Add-fillings', '1'], :input => input_json
	elsif done_task_list.include?("Add-fillings") && !done_task_list.include?("toasted")
		if input['toasted'] == "true"
			task.schedule_activity_task domain.activity_types['toasted', '1'], :input => input_json
		else
			puts "#{input['name']}'s sandwich is made!"
			task.complete_workflow_execution
		end
	elsif done_task_list.include?("toasted")
		puts "#{input['name']}'s toasted sandwich is made!"
		task.complete_workflow_execution
	end
end
```

[Click here to view the full project on Github.](https://github.com/amscotti/Simple_workflow_sandwich_maker)

From the code you can see that I need to build two functions of my own. I first needed a function that will allow me to know what tasks have been completed along with the other function that will allow me to see the original input from the order.

Reference Links,

* [Amazon SWF Documentation](http://aws.amazon.com/documentation/swf/)

If you have any questions, comments, or ways to improve this code please feel free to post in the comments.