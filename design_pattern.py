Basic Design Patterns

creational
    singleton
    prototype
    builder
    factory
structural
    facade
    proxy
behavioral
    iterator
    observer
    mediator
    state


creational - how objects are created
    how we are creating object of a certain class
    to use that - in the program, 

    singleton
        type of object, that is instantiated only once, and cant be instantiated again, even if we try to re-instantiate, it will not work

        settings class - for global settings data
        creating private constructor - cant be created again using new keyword

        static get instance method - that will check if instance is already created, if not it will create a new once - 
        if (!Settings.instance)
            Settings.instance = new Settings();

        return Settings.instance - it will return the same instance again and again - if new is required to be created - it will create a new one

        in js, we have object literals, or constant global objects 
        that are passed around by reference 

        lean on to your language built in features before implementing fancy design pattern

    prototype - clone
        inheritance - a class can be extened with a subclass - 
        problem - it can lead to complex hierarchy - that is difficult to find what inherited from what
        prototype method - is an alternative to inheritance
        instead of inheriting a functionality from a class, it comes from an object thats already been created 

        this creates flat prototype chain - that makes it easier to share functionality between objects, 

        JS - 
        zombie - eatbrain - prototype
        const chat = Object.create(zombie, name: value: chad)
        if we log the object, we will see the name, and not eat brain 
        but still can access the eat brain method 
        js will try to reach prototype chain, until it reaches the root looking for that object to be called

        dont use
        chad.__proto__; // not a modern practice
        Object.getProtoypeOf(chad)
- 

        prototype refers to its constructor - can add functionality to given class instance
        Array.prototype.bad = function() {
            console.log('I m Bad');
        }

    builder
        hot dog stand, a customer just places order - what he needs in his hotdog burger 
        - all that is added in the constructor itself, - that works but 
        hard to track all the options, 
        burger(true, true, true)

        but with builder model, we add the attributes using functions
        class hotdog():
            def _init__():
                pass
            def add_kethctup():
                pass
            def add_mustard():
                pass
            def add_kraut():
                pass

        but in js, the this, or self is returned
        that allows us to chain the methods
        thats nice way, to add multiple things in instance, to get things fixed
    factory
        instead of using the new keyword, to instantiate an object, you use a function or method to do so, 
        creating cross platform app

        class IOS
        class Android

        === checks for the type as well, '1'===1 is false, but '1'==1 is true
        const button1 = os === 'ios' ? new IOS() : new Android() 
        const button1 = os === 'ios' ? new IOS() : new Android() 
        const button1 = os === 'ios' ? new IOS() : new Android() 

        thats not maintainable 

        create a function - that will decide what type of object to create

        class ButtonFactory()
            def create_button(string: iosbutton, android button):
                if os == ios:
                    return new IOS
                else:
                    return new Android
        factory = ButtonFactory()
        btn = factory.create_button(os)
        btn = factory.create_button(os)

structural - how objects relate to each other 
    facade
        facade is the face of the building
        inside the building, there is all shenanigans, complexity
        outside we are just looking the basic things

        simplified api to hide low level details

        class PlumbingSystem():
            // low level access to plumbing system
            set_pressure(v):
                pass
            turn_on()
            turn_off()

        class ElectricalSystem():
            // low level access to electrical system
            set_voltage(v):
                pass
            turn_on()
            turn_off()

        class House {
            // people in the house don't need this low level access
            so we create a function to cover all hidden ite,s, and wrap that in a function that will take care of all the operations required
            private Plumbing = new PlumbingSystem()
            private electrical = new ElectricalSystem()

            turn_on_systems(){
                this.electrical.set_voltage(120)
                this.electrical.turn_on()
                this.plumbing.set_pressure()
                this.plumbing.turn_on
            }
            shutdown(){
                this.electrical.turn_off()
                this.plumbing.turn_off()
            }
        }

        all package installed, is facade - jquery

    proxy
        substitute
        substitute teacher when the original teacher didnt come 
        to replace the real teacher
        we can replace target object in programming - with proxy 
        reactivity system 
        update the data on UI, frontend when data changes 
        view create proxy - when changes happen
        it gets updated in the original frontend
        proxy also used when - the target object is very difficult to copy or modify as it is heavy



behavioral - how connect with each other
    iterator
                pull based system 
        traverse the collection of object
        abstractions to loop over item 
        no range function in js

        function range(start, red, step){
            return {
                [Symbol.iterator](){
                    return this;
                }
                // use it with for of
                symbol iterator object 

                next() {
                    if (start,end){
                        start = start + step
                        return {value: start, done: false}
                    }
                    return {done:true, value: end}
                }
            }
        }
    observer
        push based system
        one to many relationship 
        allows many object to subscribe to event broadcasted by one object
        bunch of receivers
        firebase, apple, js, cpp 
        all the client apps are subscribed, and get the updated data
        rjxs library
        subject class
        subscriptions to that 
        
        subject will keep track of subscriptions, 
        and call their callback functions, when the data changes

        import { Subject } from 'rxjs';
        const news = new Subject();

        const tv1 = news.subscribe(v => console.log(v+'via Den TV')
        const tv2 = news.subscribe(v => console.log(v+'via Batcave TV')
        const tv1 = news.subscribe(v => console.log(v+'via Den TV')
        
        we can call the next function, with some variable value

        news.next('Breaking news')
        news.next('the war is over')

        every subscription will be notified with time
        loop - that unfolds over time

    mediator
        middleman or broker 
        aeroplanes, and runways

        class Airplaine{
            land()
        }

        class Runway{
            clear: boolean
        }

        const runway25A = new Runway()
        const runway25B = new Runway()
        const runway7 = new Runway()

        const a = new Airplaine()
        const b = new Airplaine()
        const c = new Airplaine()

        have to figure out, if the plane can land at the runway clearly or not

        all these objects have to communicate with each other
        many to many relationship
        that is dangerous in real life and programming
        all planes cant ask all runways if its free or not

        class Tower()
            clear_for_landing(runway, plane)
                if runway.clear
                    console.log(`plane ${plane} is clear for landing`)
        
        coordination and communication between all the planes and runways


        express
        request - middleware - response 
        that sits in between to provide response

        intercepting every request like aeroplanes
        and transforms it to proper format 
        that follows the response
        clear - avoid duplciation

    state
        when object behaves differently based on many number of states

        class Human{
            think(mood)
                switch (mood){
                    case happy 
                        i am happy
                    case sad:
                        i am sad
                    default:
                        i am neutral
                }
        switch hell, not scale well
        }

        have separate class for each possible state
        inside each class, there will be same function with some name
        identical method 
        that behaves as per the class

        # abstract class
        interface State{
            think(): string;
        }

        class Happy_State implements State{
            think(){
                i am happy
            }
        }

        class Sad_State implements State{
            think(){
                i am sad
            }
        }

        class Human{
            state: State; # state as a property, its method will change

            constructor(){
                this.state = new Happy_State():
            }
            think() {
                return this.state.think()
            }
        }
        changeState(state):
            this.state = state

        can easily change the state, without any issue
        or having multiple if else cases