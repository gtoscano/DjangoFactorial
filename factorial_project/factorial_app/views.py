import subprocess
from rest_framework.views import APIView
from rest_framework.response import Response

class FactorialView(APIView):
    def get(self, request, number):
        result = self.calculate_factorial(number)
        return Response({"number": number, "factorial": result})

    def calculate_factorial(self, number):
        result = subprocess.run(["./src/factorial", str(number)], stdout=subprocess.PIPE)
        return int(result.stdout)

