<h2 align="center">
  sdRDM Markdown Syntax
</h2>

<p align="center"> 
This is an example of how to set up a data model using the Software-Driven Research Data Management (sdRDM) library which is based on abstract object models. Furthermore, the sdRDM library supports the conversion of data models defined in the Markdown format.</p>

### ✍️ Syntax

Data models defined in the Markdown format follow these conventions:

- **Title** of the data model is denoted by a heading level 1 ```#```
- **Modules** are denoted by a heading level 2 ```##```
- **Objects** are started with a heading level 3 ```###``` 
- Each object contains **fields** as a list &rarr; ```- name```
- **Required fields** are set by making the field bolt &rarr; ```- __name__```
- Each field has **options** as a list of name to value mapping &rarr; ```- Type: string```

### ⚙️ Field options

Each field in an object can hold options relevant for mapping to another data model (e.g. a standardized format) and general information such as its type and description. In the following is a collection of all native and required fields:

- **Type** - Required option to denote the data type. Please note, this can also contain other objects defined in this document.
- **Multiple** - Whether or not this field can contain multiple values. Setting to ```True```will result in a ```List[dtype]``` annoatation in the software.
- **Description** - Required option to describe the field. This should be a brief description that explains what the attribute is about.

### 🧬 Inheritance

In order to inherit attributes to another object, the object definition additionally includes the name of the parent object in italic wrapped with brackets:

&rarr; ```## Child [_Parent_]```

In the following an example data model is defined using above rules. Feel free to use this example also as a template for your own application.

---------
# ExampleDataset

This is the place where you can describe the complete dataset and give information about all the details. Markdown offers a convenient way to enable as much space as needed to elucidate purpose and capabilities of your data model.

## Objects

Level two heading allows you to group multiple classes to modules. They also allow to introduce enumerations to define a set of values for objects.

### Root

This is the root of the data model and contains all objects defined in this example. While its good practice to have a single root, you can define as many roots as you like. Furthermore, the name does not have to be ```Root``` and can be any other name.

- description
  - Type: string
  - Description: Describes the content of the dataset.
  - Dataverse: pyDaRUS.Citation.description.text
- __title__
  - Type: string
  - Description: Title of the work
  - Dataverse: pyDaRUS.Citation.title
- subject
  - Type: string
  - Description: Subject of matter linked to the dataset
  - Multiple: True
  - Dataverse: pyDaRUS.Citation.subject
- authors
  - Type: Author
  - Multiple: True
  - Description: Authors of this dataset.
- parameters
  - Type: Parameter
  - Multiple: True
  - Description: Parameters to start and configure some process

### Author

This is another object that represents the author of the dataset. Please note, that the options here contain all required fields but also custom ones. In this example, the ```Dataverse``` option specifies where each field should be mapped, when exported to a Dataverse format. Hence, these options allow you to link your dataset towards any other data model without writing code by yourself.

- __name__
  - Type: string
  - Description: Full name including given and family name
  - Dataverse: pyDaRUS.Citation.author.name
- affiliation
  - Type: string
  - Description: To which organization the author is affiliated to
  - Dataverse: pyDaRUS.Citation.author.affiliation
  
### Parameter

This is another object used to describe the parameters of given dataset. As a final note, it is important to use the description of an object to its fullest. As you might noticed, the space in between the object definition ```###``` can be freely used to describe what this object is actually about. Ultimately, this gives you the opportunity to ensure users completely understand what the intention and use case of this object is in a readable way.

- key
  - Type: string
  - Description: Name of the parameter
  - Dataverse: pyDaRUS.Process.method_parameters.name
- value
  - Type: float
  - Description: Respective value of a parameter
  - Dataverse: pyDaRUS.Process.method_parameters.value
- unit
  - Type: Units
  - Description: Unit of the parameter

## Enumerations

### Units

```python
s = "s"
m = "m"
mol = "mol"
K = "K"
A = "A"
cd = "cd"
kg = "kg"
```
