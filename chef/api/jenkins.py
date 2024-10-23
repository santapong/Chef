from jenkinsapi.jenkins import Jenkins

jenkins_url = 'http://localhost:8080'
username = ''
password = ''

jenkins = Jenkins(jenkins_url, username=username, password=password)

job_name = ''
job = jenkins.get_job(job_name)

# Trigger the build
job.invoke()