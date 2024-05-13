# Web Stack Debugging #4

## Overview:

In this web stack debugging task, we are evaluating the performance of our web server setup, which features Nginx, under pressure. Unfortunately, the results are less than satisfactory as we are encountering a significant number of failed requests.

## Benchmarking with ApacheBench:

For benchmarking purposes, we have employed ApacheBench, a widely used tool in the industry for simulating HTTP requests to a web server. In this scenario, we will be sending 2000 requests to our server, with 100 requests being sent concurrently. However, it's concerning to note that out of these requests, 943 have failed.

## Action Plan:

It's evident that our web stack requires optimization to address these failed requests and enhance its performance. We need to investigate and rectify the underlying issues to ensure that our stack operates smoothly and efficiently. As the adage goes, "when something is going wrong, logs are your best friends," so we will utilize logging extensively to pinpoint and resolve the issues.

Let's work together to troubleshoot and optimize our web stack to achieve a successful outcome with zero failed requests.

**Remember:** Logs play a crucial role in debugging and identifying issues. Keep an eye on them!
