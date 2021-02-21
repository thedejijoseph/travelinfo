We're in a country, a federation of states.

Movement is unrestricted in this country, and we want to help people find their way to/through states.

Transport has three major components: the vehicle, the way, and operations. We need to organise raw data spanning these components into useful information.

Movement occurs from one terminal in a state to another terminal in another state over a route in a vehicle.

From Park A to Park B over roads in a bus.

From Airport A to Airport B in the air in an airplane.

Let's call this a journey.

A complete journey though can have more than one journeys though.

From Park A to Park B in a car, on to Airport C to Airport D in an airplane.

Now, how to model this data and get useful results from them?

---

Terminals are in states.

Terminals are of different types and can only connect with other terminals of the same type.

The distance between two terminals is represented by travel time, in number of hours.

The primary query is to travel from one state to another.

Other qualifiers could be specified such as using only a type of terminal, or that travel time should be minimised.

---

I want to start out by simply connecting one state to another: only one journey legs. From one random terminal in a state to another.

These terminals have metadata describing what other terminals they connect to.

---

### Database Schema

`states`
```javascript
{
    name: Ondo,
    state_id: ondo,
    terminals: [
        '<terminal_id>',
        '<terminal_id>'
    ]

}
```

`terminals`
```javascript
{
    terminal_id: '<unique_id>',
    type: 'one of road, air, rail',
    state: '<state_id>',
    name: Ondo Garage,
    location: 'Approximate location: Ondo road, Akure',
    description: 'Other details',
    dest_terminals: [
        '<terminal_id>',
        '<terminal_id>'
    ]
}
```

### API and Queries

A request of

```
GET /query?from_state=ondo&to_state=lagos
```

to get a response of

```javascript
{
    from_state: Ondo,
    to_state: Lagos,
    from_terminal: {
        terminal_id: '<terminal_id>',
        name: 'Terminal name',
        location: 'Terminal location'
    },
    to_terminal: {
        terminal_id: '<terminal_id>',
        name: 'Terminal name',
        location: 'Terminal location'
    }
}
```

**Note!** The API to add/edit is on a different service. So, for testing purposes, I'll just create a script to autofill data, I guess.
