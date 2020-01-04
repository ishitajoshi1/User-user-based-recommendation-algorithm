# User-user-based-recommendation-algorithm
Recommender Algorithm is designed to predict or filter preferences based on user choices' and product ratings in Python.
# Introduction
The data consists of three csv files:

a) eProducts: This consists of product description consisting of product name, category, product id(pid) and warranty. Here, PID is unique for each product.

b) eUsers: This consists of user description consisting of product id, username, email address,ratings,warranty_left and service tag. Here, user_id(email address) is unique for each user.

c) ePscoring: This table is constructed in order to overcome the drawback of non-popularity of new products. It is built on similarity among different categories wherein PID is scored against similar categories. (5:- highly correlated)
# Optimisation
The data matrix feature is added to overcome test cases namely: 

a) New product with zero ratings

b) New User with no history

Also, the complexity of algorithm is reduced from O(no._of_categories*no._of_products) to O(no._of_categories)

# Contact me
For further queries and questions, mail me at mishitajoshi@gmail.com
