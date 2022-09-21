# Table listings and constraints with them

In this we will have 6 total table
1. The builds
2. CPU
3. GPU
4. Ram
5. Storage 
6. Motherboards

## Now I will list all of the attributes and the constraints that they need.

1. the builds
Will have 3 sections
    Build number which cannot be Null.
    Number of items
    total cost
    primary key is the build number

Everything inside of the databases are liked to the item numbers and the build numbers.

2. CPU
Will have 6 sections
    Build number cannot be null
    item number cannot be null
    brand cannot be null
    price
    name
    number of cores
    primary key is the build number and the item number
    foreign key is the build number from builds section

3. GPU
Will have 7 sections
    Build number cannot be null
    item number cannot be null
    brand cannot be null
    price
    name
    overclock
    ports
    primary key (itemnum, buildnum),
    unique (name),
    foreign key (buildnum) references Builds(buildnum)

4. Ram
Will have 7 sections
    Build number cannot be null
    item number cannot be null
    brand cannot be null
    price
    name
    type
    GB's
    primary key (itemnum, buildnum),
    foreign key(buildnum) references Builds(buildnum)

5. Storage
Will have 6 sections
    Build number cannot be null
    item number cannot be null
    brand cannot be null
    price
    name
    total
    primary key (itemnum, buildnum),
    foreign key(buildnum) references Builds(buildnum)

6. motherboard
Will have 7 sections
    Build number cannot be null
    item number cannot be null
    brand cannot be null
    price
    name
    number of ports
    size
    primary key (itemnum, buildnum),
    foreign key(buildnum) references Builds(buildnum)