# Packaging Model For Deployment
- Production Code is designed to be deployed to end user.
- In this phase we move from research code to the production code.

### Production Code Considerations
- Testability and Maintainability
- Scalability and Performance
- Reproducubility

<hr>

### Code Mapping
![alt text](images/image.png)

<hr>

### Best Practices

<img src="images/0EFCAD0B-3B7C-4B30-B986-0BE67A6B2C41_4_5005_c.jpeg">
<img src="images/47237E78-E8F2-4A98-A2B4-4ACD42C222D4_1_102_o.jpeg">

# Poetry
```
poetry add pytest
poetry show
poetry add requests@2.12.1
poetry remove requests

poetry add requests^2.12.1
poetry add requests~2.12.1
poetry install
poetry shell

poetry version minor
```