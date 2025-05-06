from TestResult import TestResult
from TestLoaderTest import TestLoaderTest
from TestLoader import TestLoader
from TestRunner import TestRunner

#result = TestResult()
#loader = TestLoader()
#suite = loader.make_suite(TestLoaderTest)
#suite.run(result)
#print(result.summary())


loader = TestLoader()
suite = loader.make_suite(TestLoaderTest)

runner = TestRunner()
runner.run(suite)