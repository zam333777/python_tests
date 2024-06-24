# Description:
 - CRUD tests for the post`s endpoint
 - All posts example is stored in the source/map_with_posts.py
 - Prepared data for the tests is stored in the source/prepared_data.py
 - Test methods are stored in the source/test_methods.py
 - Properties for the project can be configurated in the source/property.ini

# Tests Run details:
 - All tests you can find in the tests/tests.py
 -  Configure project settings. Setup SDK = Python 3.10 (Python 3.12.4) - find attached screen (project_settings.jpg)
 -  Check faker lib (plugin) is installed
 -  Run test by command in the terminal: pytest -v tests\tests.py

##  Version: 20240622 - 001

## Tests included in this file are:
- test_get_all_posts_from_endpoint
- test_negative_get_post
- test_negative_get_post_wrong_data
- test_new_post
- test_new_post_max_size_data
- test_new_post_overload_data
- test_delete_post
- test_delete_invalid_post (test failed. need to ask details about expected result)
- test_delete_post_with_null_endpoint
- test_update_post
- test_update_post_overload_data
- test_update_post_max_data

## History: 
20240622 - 001 -author - Initial version. Test are created for the post`s endpoint.
