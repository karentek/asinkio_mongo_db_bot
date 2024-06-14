from dotenv import load_dotenv
from datetime import datetime, timedelta
from config import COLLECTION
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('agregation.py started')
logger.info('Try to environment variables')


def aggregate_salaries(dt_from, dt_upto, group_type):
    logger.info('agregation function started')
    dt_from = datetime.fromisoformat(dt_from)
    dt_upto = datetime.fromisoformat(dt_upto)

    if group_type == 'hour':
        interval = timedelta(hours=1)
        date_format = '%Y-%m-%dT%H:00:00Z'
    elif group_type == 'day':
        interval = timedelta(days=1)
        date_format = '%Y-%m-%dT00:00:00Z'
    elif group_type == 'month':
        interval = timedelta(days=30)
        date_format = '%Y-%m-01T00:00:00Z'

    all_intervals = []
    current = dt_from
    while current <= dt_upto:
        all_intervals.append(current)
        current += interval

    pipeline = []

    pipeline.append({
        '$match': {
            'dt': {
                '$gte': dt_from,
                '$lte': dt_upto
            }
        }
    })

    pipeline.append({
        '$group': {
            '_id': {'$dateToString': {'format': date_format, 'date': '$dt'}},
            'total': {'$sum': '$value'}
        }
    })

    logger.info('Try to agregate collection')
    result = list(COLLECTION.aggregate(pipeline))

    result_dict = {record['_id']: record['total'] for record in result}

    labels = [interval.strftime(date_format) for interval in all_intervals]
    dataset = [result_dict.get(label, 0) for label in labels]
    logger.info('Labels and dataset is ready')
    return {'dataset': dataset, 'labels': labels}


input_data = {
   "dt_from": "2022-02-01T00:00:00",
   "dt_upto": "2022-02-02T00:00:00",
   "group_type": "hour"
}


if __name__ == '__main__':
    result = aggregate_salaries(
        input_data['dt_from'],
        input_data['dt_upto'],
        input_data['group_type']
    )
    logger.info(result)




