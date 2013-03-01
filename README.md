python-access
=============

Access modifiers for instance methods of python classes.

Modifiers
---------

- `private` — private methods are accesible only within the class in which they are declared.
- `protected` — protected methods are accesible from within the class in which they are declared, and from within any class derived from that class.
- `public` — public methods have no restrictions on access (decorator does nothing).

Usage
-----

    from access import private, protected

    class A:

        @private
        def private_method(self):
            pass

        @protected
        def protected_method(self):
            pass
