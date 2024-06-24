# Description:
 - CRUD tests for the posts endpoint
 - All posts example are stored in the source/map_with_posts.py
 - Prepared data for the tests is stored in the source/prepared_data.py
 - Test methods are stored in the source/test_methods.py
 - Properties for the project can be configurated in the source/property.ini

# Tests Run details:
 - All tests you can find in the tests/tests.py
 -  Configure project settings. Setup SDK = Python 3.10 (Python 3.12.4) - find atached screen (project_settings.jpg)
 -  Check faker lib (plugin) in installed
 -  Run test by command in the terminal: pytest -v tests\tests.py

##  Vesion: 20240622 - 001

## Tests included in this file are:
 1.test_get_all_posts_from_endpoint
 2.test_negative_get_post
 3.test_negative_get_post_wrong_data
 4.test_new_post
 5.test_new_post_max_size_data
 6.test_new_post_overload_data
 7.test_delete_post
 8.test_delete_invalid_post
 9.test_delete_post_with_null_endpoint
 10.test_update_post
 11.test_update_post_overload_data
 12.test_update_post_max_data

## History: 
20240622 - 001 -author - Initial version. Test are created for the posts endpoint.
