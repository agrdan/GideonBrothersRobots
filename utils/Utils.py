from datetime import date
import datetime
from datetime import datetime as dt


class Utils:

    @staticmethod
    def parseStringDtToDate(string_date):
        try:
            date_formate = datetime.datetime.strptime(string_date, '%Y-%m-%d')
            parsedDate = date_formate.strftime("%Y-%m-%d")
            return parsedDate
        except Exception as e:
            print(e)

    @staticmethod
    def parseTimestamp(timestamp):
        date = dt.fromtimestamp(int(timestamp))
        parsedDate = date.strftime("%Y-%m-%d")
        return parsedDate