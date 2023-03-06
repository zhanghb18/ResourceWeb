from flask import jsonify

class JSONWrapper(object):
    @staticmethod
    def fill_result(data, status, msg, http_code=200):
        result = {
            'data': data,
            'status': status,
            'msg': msg
        }
        return jsonify(result), http_code

    @staticmethod
    def success(data=''):
        return JSONWrapper.fill_result(data, 0, 'success')

    @staticmethod
    def success_with_status(status):
        return JSONWrapper.fill_result('', status, 'success')

    @staticmethod
    def success_with_data_and_status(data='',status=0):
        return JSONWrapper.fill_result(data,status,'success')

    @staticmethod
    def fail(exception_info=None, http_code=200, status=1):
        #return JSONWrapper.fill_result('', exception_info.STATUS, exception_info.MSG)
        return JSONWrapper.fill_result(exception_info, status, 'error', http_code)
