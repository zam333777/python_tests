#------------------------Imports---------------------------------------------------------------
import pytest
import configparser
from ..sources import map_with_posts
from ..sources import test_methods
from ..sources import prepared_data

config = configparser.ConfigParser()
config.read('sources/property.ini')
base_url = config['DEFAULT']['url']
#------------------------Fixtures---------------------------------------------------------------
@pytest.fixture()
def setup_teardown(request):
    #tearDown after case with post and update methods.
    #return data as it was before testing (data before tests is located in map_with_posts.py file)
    yield
    post_id_to_delete = getattr(request.node, "post_id_to_delete", None)
    post_id_return_data = getattr(request.node, "post_id_return_data", None)
    if post_id_to_delete is not None:# delete post after test
        delete_response = test_methods.delete_query(base_url, post_id_to_delete)
        assert delete_response.status_code == 200
    else:
        if post_id_return_data is not None: # return data as it was before testing (data before tests is located in map_with_posts.py file)
            new_data = {
                'userId': map_with_posts.map_with_posts['map_'+post_id_return_data+'']['userId'],
                'title': map_with_posts.map_with_posts['map_'+post_id_return_data+'']['title'],
                'body': map_with_posts.map_with_posts['map_'+post_id_return_data+'']['body']
            }
            update_response = test_methods.update_query(base_url, post_id_return_data, new_data)
            assert update_response.status_code == 200
            assert test_methods.get_query(base_url, post_id_return_data, 'title', 'body') == [new_data['title'], new_data['body']]





#------------------------Tets with GET methods ----------------------------------------------

#check all posts from the endpoint.The endpoint has 100 posts.Compare the response with the map_with_posts.py file
def test_get_all_posts_from_endpoint():
    for i in range (1, 101):
     response = test_methods.get_query(base_url, str(i), 'id', 'userId', 'title', 'body')
     elements = ['id', 'userId', 'title', 'body']
     assert response == [map_with_posts.map_with_posts['map_'+str(i)+''][element] for element in elements], f"Assertion failed for map_{i}, continuing with next iteration"

#get a non existing post  from the endpoint. Negative case
def test_negative_get_post():
    response = test_methods.get_query_negative(base_url, '102')
    assert response is not None, f"Test failed: {response}"
    assert response.status_code == 404, f"Test failed: {response.status_code}"

#get a post with wrong data from the endpoint. Negative case
def test_negative_get_post_wrong_data():
    response = test_methods.get_query_negative(base_url, '_1_!*8:;%3')
    assert response is not None, f"Test failed: {response}"
    assert response.status_code == 404, f"Test failed: {response.status_code}"



#------------------------Tets with POST methods ----------------------------------------------

#get a post with wrong data from the endpoint
def test_new_post(setup_teardown, request):
    response = test_methods.post_query(base_url, '/', prepared_data.data)
    assert response is not None, f"Test failed: {response}"
    assert response['body'] == prepared_data.data['body'], f"Test failed: {response['body']}"
    assert response['title'] == prepared_data.data['title'], f"Test failed: {response['title']}"
    request.node.post_id_to_delete = str(response['id'])

#check max uboundaries for the post data
def test_new_post_max_size_data(setup_teardown, request):
    response = test_methods.post_query(base_url, '/', prepared_data.max_data)
    assert response['body'] == prepared_data.max_data['body'], f"Test failed: {response}"
    request.node.post_id_to_delete = str(response['id'])

#check overloaded data for the post data (more than 9999999 chars for body and 999999 chars for title. Negative case
def test_new_post_overload_data():
    response = test_methods.post_query(base_url, '/', prepared_data.big_data)
    assert response.status_code == 500, f"Test failed: {response}"




#------------------------Tets with DELETE  methods ----------------------------------------------

#delete a post from the endpoint
def test_delete_post():
    response = test_methods.delete_query(base_url, '102')
    assert response.status_code == 200, f"Test failed: {response}"

#delete a non existing post from the endpoint. Negative case
def test_delete_invalid_post():
    response = test_methods.delete_query(base_url, '9999999')
    assert response.status_code == 404, f"Test failed: {response}"

#delete a post with null endpoint. Negative case
def test_delete_post_with_null_endpoint():
    response = test_methods.delete_query(base_url, '')
    assert response.status_code == 404, f"Test failed: {response}"






#------------------------Tets with UPDATE  methods ----------------------------------------------

#update a post from the endpoint. After test data in the post will be updated as it was before in map_with_posts.py
def test_update_post(setup_teardown, request):
    response = (test_methods.update_query(base_url, '1', prepared_data.data)).json()
    assert response['body'] == prepared_data.data['body'], f"Test failed: {response}"
    assert response['title'] == prepared_data.data['title'], f"Test failed: {response}"
    request.node.post_id_return_data = str(response['id'])

#update a post with overloaded data. Negative case
def test_update_post_overload_data():
    response_code = test_methods.update_query(base_url, '1', prepared_data.big_data)
    assert response_code == 500, f"Test failed: {response_code}"

#update a post with max data. After test data in the post will be updated as it was before in map_with_posts.py
def test_update_post_max_data(setup_teardown, request):
    response = (test_methods.update_query(base_url, '1', prepared_data.max_data_for_update)).json()
    assert response['body'] == prepared_data.max_data_for_update['body'], f"Test failed: {response}"
    assert response['title'] == prepared_data.max_data_for_update['title'], f"Test failed: {response}"
    request.node.post_id_return_data = str(response['id'])


