drop table if exists CPU;
drop table if exists GPU;
drop table if exists RAM;
drop table if exists Storage;
drop table if exists Motherboard;
drop table if exists Builds;

create table if not exists Builds
(
    buildnum  int not null,
    name        varchar(15),
    numofitems int,
    price int,
    primary key (buildnum)
);

Create table if not exists CPU
(
    buildnum    int not null,
    itemnum     int NOT NULL,
    brand       varchar(15) not null,
    price       int,
    name        varchar(25),
    numofcores  int,
    primary key (itemnum, buildnum),
    foreign key(buildnum) references Builds(buildnum)
);

create table if not exists GPU
(
    buildnum    int not null,
    itemnum     int NOT NULL,
    brand       varchar(15) not null,
    price       int,
    name        varchar(25),
    overclock   int,
    ports       varchar(3),
    primary key (itemnum, buildnum),
    foreign key (buildnum) references Builds(buildnum)
);

create table if not exists RAM
(
    buildnum    int not null,
    itemnum     int not null,
    brand       varchar(15) not null,
    price       int,
    name        varchar(25),
    type        varchar(4),
    GBs         int,
    primary key (itemnum, buildnum),
    foreign key(buildnum) references Builds(buildnum)

);

create table if not exists Storage
(
    buildnum    int not null,
    itemnum     int not null,
    brand       varchar(15) not null,
    price       int,
    name        varchar(25),
    total       int,
    primary key (itemnum, buildnum),
    foreign key(buildnum) references Builds(buildnum)

);

create table if not exists Motherboard
(
    buildnum    int not null,
    itemnum     int not null,
    brand       varchar(15) not null,
    price       int,
    name        varchar(25),
    numofports  int,
    size        varchar,
    primary key (itemnum, buildnum),
    foreign key (buildnum) references Builds(buildnum)

);
