drop table if exists users;
create table users (
  id integer primary key,
  firstname text not null,
  lastname text not null,
  email text not null,
  password text not null
);

drop table if exists guides;
create table guides (
  id integer primary key,
  firstname text not null,
  lastname text not null,
  email text not null,
  contact text not null,
  password text not null,
  address text not null,
  charge integer not null,
  rating real not null
);

drop table if exists interests;
create table interests (
  id integer primary key,
  name text not null
);

drop table if exists user_interests;
create table user_interests (
  id integer primary key autoincrement,
  user_id integer not null,
  interest_id integer not null,
  foreign key(user_id) references users(id),
  foreign key(interest_id) references interests(id)
);

drop table if exists guide_interests;
create table guide_interests (
  id integer primary key autoincrement,
  guide_id integer not null,
  interest_id integer not null,
  foreign key(guide_id) references guides(id),
  foreign key(interest_id) references interests(id)
);

drop table if exists events;
create table events (
  id integer primary key,
  description text not null,
  interest_id integer not null,
  location text not null,
  guide_id integer not null,
  start_time datetime not null,
  end_time datetime not null,
  foreign key(interest_id) references interests(id),
  foreign key(guide_id) references guides(id)
);

drop table if exists booking;
create table booking (
  id integer primary key autoincrement,
  booking_time datetime not null,
  event_id integer not null,
  user_id integer not null,
  foreign key(event_id) references events(id),
  foreign key(user_id) references users(id)
);