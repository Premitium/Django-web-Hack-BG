# HackLX

Your task is to create a small system for offers.

Here are some mockups: https://app.moqups.com/meco/FYpHUL2OUu/view/page/ad64222d5

Keep in mind:
- You have handle the media file upload
- You have to optimize you calls using django-debug-toolbar
- You have to use Bootstrap to make the system look good.

# What is it about:

- Class-based views
  So far all views were functions that accept a request object and return a response object.
  Class-based views are very similar the however, are classes and can be inherited and extended.
  You can reuse the functionality of a super class in a child class.
  If you have a monotonous job on your hands like showing all records from a database in a list - > ListView

- The super()
  Use it for multi-inheritance. Including common idioms like mixins, interfaces, abstract classes, etc.
  Call the __init__ method of the parent base class first.
  //TO DO: look over inheritance


- Using mixins with Django
  Mixins are a controlled way of adding functionality to classes.
  They are not a special language construct.
  Mixins offer modularity and this is why we use them.
  If a feature doesn't exist in many classes and we want to use it there.
   - one single responsibility
   - not meant to be extended
   - not meant to be instantiated
  In Python the concept of mixins is implemented using multiple inheritance
   - The order of inheritance matters
      class Foo(BaseFoo, SomeMixin):
          pass
      SomeMixi is a base class, extended by BaseFoo, extended by Foo
