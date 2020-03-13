from time import sleep
from os import system, path
import json
import schedule as sch

if not path.exists('/rclone.conf'):
    raise Exception(f'Missing /rclone.conf')

# read file
with open('/config.json', 'r') as conf:
    conf_json = conf.read()

# parse file
config_jobs = json.loads(conf_json)


def do_something(name: str, location: str, bucket: str):
    def inner_do_something():
        if not path.exists(location):
            raise Exception(f'Location is not available within container: {location}')
        result = system(f'rclone sync {location} {name}:{bucket} --config=/rclone.conf --fast-list -P')
        print(f'result is: {result}')

    return inner_do_something


for job in config_jobs.keys():
    job_dict = config_jobs[job]
    sch.every().day.at(job_dict.get('time')).do(do_something(job, job_dict.get('location'), job_dict.get('bucket')))

while True:
    sch.run_pending()
    sleep(1)
