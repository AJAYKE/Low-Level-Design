## Strategy Pattern

Strategy Pattern is all about identifying the changing behaviours in the object and seperating and defining thier own objects, this helps in avoiding hard coding in the main class, and helps in keeping the codebase modular and objects pluggable

The strategy pattern is about:

1. Identifying Changing Behaviors:

   Recognize parts of your system that vary (e.g., flying or quacking behavior in ducks).

2. Encapsulating the Variation:

   Define these behaviors as separate classes (e.g., FlyWithWings, FlyNoWay) rather than hardcoding them into the main class (Duck).

3. Promoting Reusability:

   These behavior classes can be reused across different contexts or objects (e.g., multiple types of ducks can share FlyWithWings or Quack).

4. Flexible Composition:

   Instead of inheritance to define behavior, you use composition. You "compose" the main object (Duck) with the required behavior at runtime. This avoids rigid inheritance hierarchies.
