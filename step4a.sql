drop table if exists bought;

insert into Builds values(1, 'Foundation', 6, 799);
insert into Builds values(2, 'Creator Plus', 6, 3499);
insert into Builds values(3, 'Streaming Plus', 6, 1899);
insert into Builds values(4, 'H1 Mini Pro', 6, 1699);
insert into Builds values(5, 'Starter Pro', 6, 1299);

insert into CPU values(1, 6, 'AMD', 180, 'Ryzen 5600G', 6);
insert into CPU values(2, 7, 'Intel', 600, 'i9-12900k', 16);
insert into CPU values(3, 8, 'AMD', 449, 'Ryzen 7 5800X', 8);
insert into CPU values(4, 9, 'Intel', 290, 'i7-10700kf', 8);
insert into CPU values(5, 10, 'Intel', 125, 'i5-10400f', 6);

insert into GPU values(1, 11, 'AMD', 180, 'Ryzen 5600G', 2.3, 2);
insert into GPU values(2, 12, 'NVIDIA', 1119, 'GeForce RTX 3080 Ti', 14, 4);
insert into GPU values(3, 13, 'NVIDIA', 849, 'GeForce RTX 3070 Ti', 15, 4);
insert into GPU values(4, 14, 'NVIDIA', 399, 'GrForce RTX 3060 Ti', 20, 4);
insert into GPU values(5, 15,'NVIDIA', 399, 'GrForce RTX 3060 Ti', 18, 4);

insert into RAM values(1, 16, 'Patriot',  48.99, 'Viper Steel', 'DDR4', 8);
insert into RAM values(2, 17, 'T-Force', 79.99, 'Delta RGB', 'DDR4', 16);
insert into RAM values(3, 18, 'Patriot',  69.99, 'Viper Steel', 'DDR4', 8);
insert into RAM values(4, 19, 'T-Force', 79.99, 'Delta RGB', 'DDR4', 16);
insert into RAM values(5, 20, 'T-Force', 55.99, 'Vulcan Z', 'DDR4', 8);

insert into Storage values(1, 21, 'Samsung', 69.99, '9800 NVMe SSD', 500);
insert into Storage values(2, 22, 'Western Digital', 109.99, 'SN850', 1000);
insert into Storage values(3, 23, 'Samsung', 219.99, '970 Evo plus', 2000);
insert into Storage values(4, 24, 'Samsung', 119.99, '970 evo', 1000);
insert into Storage values(5, 25, 'Western Digital', 94.99, 'SN550', 1000);

insert into Motherboard values(1, 26, 'Gigabyte', 129.99, 'B550 gaming x v2', 6, 'full size');
insert into Motherboard values(2, 27, 'MSI', 199.99, 'Pro Z690', 18, 'full size');
insert into Motherboard values(3, 28, 'Gigabyte', 129.99, 'B550 gaming x v2', 6, 'full size');
insert into Motherboard values(4, 29, 'MSI', 169.99, 'B560i ITX', 9, 'Mini');
insert into Motherboard values(5, 30, 'ASUS', 119.99, 'Prime b560-plus', 15, 'full size');

drop table if exists alice_pur;
create table alice_pur(
  name varchar(25),
  price int,
  primary key (name)
);
insert into alice_pur(name, price)
select name, price
from Builds
where Builds.buildnum=2;

insert into alice_pur(name, price)
select name, price
from GPU
where GPU.buildnum=2;

insert into alice_pur(name, price)
select name, price
from Storage
where Storage.brand='Western Digital';

create table bought(
  buildnum int not null,
  itemnum int not null,
  numbought int,
  primary key(itemnum),
  foreign key(buildnum) references Builds(buildnum)
);

insert into bought values(1, 1, 40);
insert into bought values(2, 2, 80);
insert into bought values(3, 3, 20);
insert into bought values(4,4, 30);
insert into bought values(5, 5, 44);
insert into bought values(1, 6, 12);
insert into bought values(2, 7, 18);
insert into bought values(3, 8, 9);
insert into bought values(4, 9, 2);
insert into bought values(5, 10, 27);
insert into bought values(1, 11, 1);
insert into bought values(2, 12, 20);
insert into bought values(3, 13, 15);
insert into bought values(4, 14, 10);
insert into bought values(5, 15, 5);
insert into bought values(1, 16, 22);
insert into bought values(2, 17, 14);
insert into bought values(3, 18, 5);
insert into bought values(4, 19, 30);
insert into bought values(5, 20, 29);
insert into bought values(1, 21, 11);
insert into bought values(2, 22, 9);
insert into bought values(3, 23, 31);
insert into bought values(4, 24, 17);
insert into bought values(5, 25, 26);
insert into bought values(1, 26, 8);
insert into bought values(2, 27, 21);
insert into bought values(3, 28, 15);
insert into bought values(4, 29, 33);
insert into bought values(5, 30, 15);

select max(numbought)
from bought b;
drop table if exists cart;
create table cart
(
    name varchar(25),
    price int
);

drop table if exists reviews;
create table reviews
(
    buildnum int,
    itemnum int,
    review varchar(100)
);

insert into reviews values(1, 1, 'Great starter PC');
insert into reviews values(2, 2, 'Very expensive but amazing');
insert into reviews values(3, 3, 'be the first to write a review');
insert into reviews values(4, 4, 'the best small pc on the market');
insert into reviews values(5, 5, 'Best starter PC');
insert into reviews values(1, 6, 'Very good for gaming');
insert into reviews values(2, 7, 'doesnt have enough cores');
insert into reviews values(3, 8, 'Better than most for gaming');
insert into reviews values(4, 9, 'Be the first to write a review');
insert into reviews values(5, 10, 'Be the first to write a review');
insert into reviews values(1,11, 'Not enough for graphics');
insert into reviews values(2, 12, 'best on the market');
insert into reviews values(3, 13, 'not very much overclock beut very good');
insert into reviews values(4, 14, 'very good with heat');
insert into reviews values(5, 15, 'be the first to review');
insert into reviews values(1,16, 'Not strong enough' );
insert into reviews values(2, 17, 'Very good for gaming');
insert into reviews values(3, 18, 'Not strong enough');
insert into reviews values(4, 19, 'Very good for gaming');
insert into reviews values(5, 20, 'Be the first to review');
insert into reviews values(1, 21, 'Not a lot of storage but fast');
insert into reviews values(2, 22, 'be the first to write a review');
insert into reviews values(3, 23, 'A lot of storage');
insert into reviews values(4, 24, 'best on the market');
insert into reviews values(5, 25, 'be the first to write a review');
insert into reviews values(1, 26, 'be the first to write a review');
insert into reviews values(2, 27, 'has many ports for everyhting you need');
insert into reviews values(3, 28, 'very powerful');
insert into reviews values(4, 29, 'best in the market for mini');
insert into reviews values(5, 30, 'very large board but very functional');