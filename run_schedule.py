import schedule, time
from engine.batch import generate_batch_sync

TOPIC = 'Samsung S24'
COUNT = 15
PUBLISH = False  # set True only if ready

def job():
    print('Scheduled job running...')
    generate_batch_sync(TOPIC, COUNT, publish=PUBLISH)
    print('Done')

# Example schedule (uncomment to use)
# schedule.every().day.at('02:00').do(job)

if __name__ == '__main__':
    print('Scheduler started. Edit run_schedule.py to set your schedule.')
    while True:
        schedule.run_pending()
        time.sleep(1)
