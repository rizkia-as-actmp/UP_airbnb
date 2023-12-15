CREATE TABLE `account` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `full_name` varchar(255) NOT NULL,
  `email` varchar(255) UNIQUE NOT NULL,
  `password` varchar(255) NOT NULL
);

CREATE TABLE `host` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `owner_id` bigint,
  `title` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `type` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL,
  `facilities` varchar(255) NOT NULL,
  `price` int NOT NULL
);

CREATE TABLE `ticket` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `holder_id` bigint,
  `host_id` bigint,
  `valid_at` timestamp NOT NULL,
  `expired_at` timestamp NOT NULL,
  `is_finish` boolean NOT NULL DEFAULT false,
  `price` decimal(60,0) NOT NULL
);

CREATE TABLE `pp` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `account_id` bigint,
  `image_bytes` mediumblob NOT NULL
);

CREATE TABLE `image` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `host_id` bigint,
  `image_bytes` mediumblob NOT NULL
);

CREATE TABLE `review` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `ticket_id` bigint,
  `writer_id` bigint,
  `host_id` bigint,
  `writer_name` varchar(255) NOT NULL,
  `comment` text NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT (now())
);

ALTER TABLE `host` ADD FOREIGN KEY (`owner_id`) REFERENCES `account` (`id`);

ALTER TABLE `ticket` ADD FOREIGN KEY (`holder_id`) REFERENCES `account` (`id`);

ALTER TABLE `pp` ADD FOREIGN KEY (`account_id`) REFERENCES `account` (`id`);

ALTER TABLE `image` ADD FOREIGN KEY (`host_id`) REFERENCES `host` (`id`);

ALTER TABLE `review` ADD FOREIGN KEY (`ticket_id`) REFERENCES `ticket` (`id`);

ALTER TABLE `review` ADD FOREIGN KEY (`writer_id`) REFERENCES `account` (`id`);

ALTER TABLE `review` ADD FOREIGN KEY (`host_id`) REFERENCES `host` (`id`);