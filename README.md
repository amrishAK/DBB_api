# DBB_api
 It is the main service for the application, it is used to create and get the posts
 
 ### Component Design
- These are  the main application services 
- The primary node receives the user requests via gateway and processes 
- Maintains the processed transactions in a from the user in a buffer and pushes it to the atomic broadcaster
- All the nodes except the primary receives the data from the atomic broadcaster

### API Url
    For creating Post
     url: ip:port/post
     method: POST
     Request JSON: {'Data' : "Test Post", "PayLoadToken" : 0.0} (Note : dont need to add payload token while calling through gatway, or fix the timeStamp as PayLoadToken)
     Response: {'result' : ""}
    
    For getting all post
     url: ip:port/post
     method: GET
     Response: {"ServerIp" : "" , "result" : []}

### Procerdure To Run
- Needed Python 3.6
- Needed c++ : Windows => c++ version 2015 | linux => install gcc-c++
- Run command to install requirements : Windows => pip install -r Requirements.txt | linux => pip3 install -r Requirements.txt
