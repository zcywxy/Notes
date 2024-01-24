# Matrix algebra concepts
- A *matrix* is a doubly-ordered arrangement of scalars. The rows represents one set of categories. The columns represent the other set of categories. "3 by 4" means 3 rows by 4 columns. The dimensions of a matrix are always presented as the **number of rows by the number of columns.**  If you want to *add matrices together or subtract* a matrix from another matrix, then the **dimensions have to be exactly the same**. 
- a *scalar*, it's just matrix, speak for a number. 
- *Identity matrix*, I, a square (same number of row and columns)
	![[Pasted image 20230712215912.png]]
- The *product* of two matrices is going to have the same number of columns is the first matrix, the row dimensions of the second matrix.
	- ![[Pasted image 20230322155548.png|300]] 
- The *inverse* of a matrix, $R^{-1}$, can provide a form of matrix division such that $R^{-1}$R=R$R^{-1}$=I 
	- ![[Pasted image 20230322161409.png|500]] ![[Pasted image 20230322161424.png|600]] 
- *Determinant* of a matrix. a determinant is as a single numerical value that represents the general variance in an entire matrix. the larger it is, the more variances you're set of items. The determinant is kind of how independent are those ten items. The problem is, is as those become increasingly highly correlated, right? Where if one item you have a really high likelihood of knowing their response and another item that determinant gets smaller and smaller and smaller, and that's a problem in the models that we're going to run into. And you will get an error and m plus that says aa near zero determinant convergence fail. What that means is you have some linear dependency in your data. At the extreme, you have two things that are correlated, 1 . 0 if I have weight in pounds and weight in kilograms, those are linear transformations. And you have a zero determinant. That means there is no generalized variance, because if you have weight in pounds, I know what you're waiting kilograms.  We rarely have that in the work that all of us do. What we have is a high correlation, . 7 . 8 . 9, and it gets near zero. That's a problem that we'll discuss. You have to have a non zero determinant in order to invert a matrix.  if you have *a zero or near zero determinant*, then you cannot invert the matrix that is called *non positive definite*. You have some kind of problem with your matrix. And it either can be a variance that's very close to zero. Or it can be a correlation that's very high among your elements.
	- ![[Pasted image 20230712222440.png]]
- *Transpose*: r* c to c* r, also called "Prime"
	- ![[Pasted image 20230322162351.png|500]]
	- ![[Pasted image 20231025123251.png|200]] 
- *symmetric matrix*, It is  square. And the elements are reflected above and below the diagonal. 
	- ![[Pasted image 20231025124841.png|300]] 
- *diagonal matrices* has to be square, because it has a diagonal. A rectangle doesn't have a diagonal on it. It has to be square to run from the upper left to the lower right to have a diagonal. And it doesn't have anything on the off diagonal. It's only aa square matrix that has values on the diagonal itself.
- All of *vector* is is a matrix with a single row or a single column. How we're gonna denote that is notice that it is *lowercase bold*. We have upper case bold as a full matrix, lowercase bold as a vector. 
      ![[Pasted image 20230712222824.png|300]]

### Design Matrix
we don't actually think that it's matrix algebra based and that there's a **design matrix** involved that we're using when we're specifying our model
![[Pasted image 20230322162727.png|500]] ![[Pasted image 20230322163036.png|500]] ![[Pasted image 20230322163218.png|500]]  ![[Pasted image 20230322163300.png|400]]  

You would use ordinary least squares regression, unweighted stuff, and to get to obtain your vector of coefficient estimates. Set up our design matrix, calculate the transpose, multiply it by the design, make yourself take the inverse of that product, calculate transpose of x and then also use the values on y to get our vector of three coefficient estimates. 
![[Pasted image 20230322165635.png|500]] ![[Pasted image 20230322170318.png|500]] ![[Pasted image 20230322170956.png|600]]  
s is the number of regression coefficients estimated in the model which is also the number of elements in $\hat{\beta}$, $\epsilon$ is the vector of residuals.
### Add and multiply
![[Pasted image 20230322155319.png|400]]  ![[Pasted image 20230322155437.png|460]]  ![[Pasted image 20230322155841.png|400]]   ![[Pasted image 20230322155855.png|400]]    
![[Pasted image 20230322155548.png]]   ![[Pasted image 20230322155643.png|600]] ![[Pasted image 20230322155707.png|400]] 

### Inverse, transpose, and diagonal matrix
      ![[Pasted image 20230322160609.png]] ![[Pasted image 20230322160653.png]]
