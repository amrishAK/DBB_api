# DBB_api
 It is the main service for the application, it is used to create and get the posts
 
 ### Component Design
- These are  the main application services 
- The primary node receives the user requests via gateway and processes 
- Maintains the processed transactions in a from the user in a buffer and pushes it to the atomic broadcaster
- All the nodes except the primary receives the data from the atomic broadcaster 

### Procerdure To Run
- Needed Python 3.6
- Needed c++ : Windows => c++ version 2015 | linux => install gcc-c++
- Run command to install requirements : Windows => pip install -r Requirements.txt | linux => pip3 install -r Requirements.txt
