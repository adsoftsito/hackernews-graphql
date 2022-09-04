from django.test import TestCase

# Create your tests here.
from links.schema import Query
from links.schema import Mutation

#from django.test.testcases import TestCase
import graphene

class AnExampleTest(TestCase):

    def setUp(self):
        super().setUp()
        self.query = """
            query {
              links {
                id
              }
            }
        """
        self.mutation = """
            mutation {
              createLink(description:"google", url:"google") {
                id
              }
            }
        """
    def test_mutation_link(self):
        schema = graphene.Schema(mutation=Mutation)
        result = schema.execute(self.mutation)
        self.assertIsNone(result.errors)
        print ("mutation ")
        print (result.data)

        self.assertDictEqual({"createLink": {"id": 2}}, result.data)


    def test_query_link(self):
        schema = graphene.Schema(query=Query)
        result = schema.execute(self.query)
        self.assertIsNone(result.errors)
        print ("query ")
        print (result.data)
        self.assertDictEqual({"links": []}, result.data)


#import json
#from graphene_django.utils.testing import GraphQLTestCase

#class MyFancyTestCase(GraphQLTestCase):
#    def test_some_query(self):
#        response = self.query(
#            '''
#            query {
#                links {
#                    id
#                }
#            }
#            ''',
#            op_name='links'
#        )


#content = json.loads(response.content.data)

        # This validates the status code and if you get errors
 #       self.assertResponseNoErrors(response)
