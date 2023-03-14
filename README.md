
Example query

`http://127.0.0.1:8081/api/v1/foods?filter=[]`

Example filter values

`filter=[">", "price", 100]`
`filter=["=", "is_vegan", "true"]`
`filter=["AND", [">", "price", 100], ["=", "is_vegan", "true"]]`