<snippet>
  <content><![CDATA[
# ${1:Class Based Views}

# HackLX

Your task is to create a small system for offers.

Here are some mockups: https://app.moqups.com/meco/FYpHUL2OUu/view/page/ad64222d5

Keep in mind:
- You have handle the media file upload
- You have to optimize you calls using django-debug-toolbar
- You have to use Bootstrap to make the system look good.

## Class-based views
  So far all views were functions that accept a request object and return a response object.
  Class-based views are very similar the however, are classes and can be inherited and extended.
  You can reuse the functionality of a super class in a child class.
  If you have a monotonous job on your hands like showing all records from a database in a list - > ListView

## The super()
  Use it for multi-inheritance. Including common idioms like mixins, interfaces, abstract classes, etc.
  Call the __init__ method of the parent base class first.
  //TO DO: look over inheritance


## Using mixins with Django
  Mixins are a controlled way of adding functionality to classes.
  They are not a special language construct.
  Mixins offer modularity and this is why we use them.
  If a feature doesn't exist in many classes and we want to use it there.
   1. one single responsibility
   2. not meant to be extended
   3. not meant to be instantiated
  In Python the concept of mixins is implemented using multiple inheritance
   1. The order of inheritance matters
      class Foo(BaseFoo, SomeMixin):
          pass
      SomeMixi is a base class, extended by BaseFoo, extended by Foo
   2. One of the first methods to be called when processing a request is dispatch()

# Common CBV features:
  1. If we want to add a feature to a CBV using a mixin sometimes we need to know more about the Django internals
  2. dispatch() takes care of the HTTP method used get/post/etc.
    - e.g. check if a user is logged in has permissions
  3. get_context_data() it passes \*\*kwargs arguments to the template context it is a way to add more context to the views
  4. get_template_names() is a method called from render to response and it lists all template names


# MRO is an acronym for Method Resolution Order.

# reverse_lazy and reverse?

## ListView - it is automatically looking for a template with the name of the model _ list.html
  1. What is the ListView context?
    - get_context_data() in list.py

  ]]></content>
    <tabTrigger>readme</tabTrigger>
  </snippet>
