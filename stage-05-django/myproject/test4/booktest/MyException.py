from django.http import HttpResponse

class CustomException():
    def process_exception(self,request,exception):
        return HttpResponse(exception.message)