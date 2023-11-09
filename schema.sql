CREATE TABLE `av_output` (
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `av_output_id` INT DEFAULT NULL,
  `av_output` VARCHAR(255) DEFAULT NULL,
  `av_output_date` DATETIME DEFAULT NULL,
  `av_output_last` VARCHAR(255) DEFAULT NULL,
  `av_output_last_date` DATETIME DEFAULT NULL,
  `av_output_family` VARCHAR(255) DEFAULT NULL,
  `av_vendor` VARCHAR(255) DEFAULT NULL
);

CREATE TABLE `dashboards` (
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL UNIQUE,
  `path` VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE `graphs` (
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `title` VARCHAR(50) NOT NULL,
  `unique_identifier` VARCHAR(25) NOT NULL UNIQUE,
  `enabled` BIT(1) NOT NULL,
  `level` INT DEFAULT NULL
);

CREATE TABLE `malicious_urls` (
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `partner_id` INT NOT NULL,
  `truncated` INT NOT NULL,
  `hash` VARCHAR(33) NOT NULL,
  `filename` VARCHAR(255) NOT NULL,
  `malicious_url` VARCHAR(1000) NOT NULL,
  `insert_datetime` DATETIME NOT NULL,
  `mds` CHAR(1) DEFAULT NULL,
  `received_date` DATETIME DEFAULT NULL,
  `mds_scan_date` DATETIME DEFAULT NULL,
  `main_location` VARCHAR(255) DEFAULT NULL,
  `siteadvisor` CHAR(1) DEFAULT NULL,
  `zeus_control` CHAR(1) DEFAULT NULL,
  `zeus_configurl` CHAR(1) DEFAULT NULL,
  `zeus_binaryurl` CHAR(1) DEFAULT NULL,
  `zeus_dropurl` CHAR(1) DEFAULT NULL,
  `zeus_fakeurl` CHAR(1) DEFAULT NULL,
  `safebrowsing` CHAR(1) DEFAULT NULL,
  `malwaredomainlist` CHAR(1) DEFAULT NULL,
  `malware_patrol` CHAR(1) DEFAULT NULL,
  `checkurl_scan_date` DATETIME DEFAULT NULL
);

CREATE TABLE `partner` (
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `our_login` VARCHAR(255) NOT NULL,
  `our_password` VARCHAR(255) NOT NULL,
  `contact_info_id` INT NOT NULL UNIQUE,
  `login_down_samples` VARCHAR(255) NOT NULL,
  `pass_down_samples` VARCHAR(255) NOT NULL,
  `url_down_samples` VARCHAR(500) NOT NULL,
  `days_not_down` INT DEFAULT NULL,
  `priority` INT NOT NULL,
  `quota` INT NOT NULL,
  `password_decompress` VARCHAR(255) DEFAULT NULL,
  `url_crawling_deep` INT NOT NULL,
  `admin_web` VARCHAR(255) NOT NULL,
  `main_location` VARCHAR(255) DEFAULT NULL,
  `main_location_code` VARCHAR(2) NOT NULL,
  `uid` INT DEFAULT NULL,
  `gid` INT DEFAULT NULL,
  `homedir` VARCHAR(255) DEFAULT NULL,
  `shell` VARCHAR(255) DEFAULT NULL,
  `latitude` FLOAT DEFAULT NULL,
  `longitude` FLOAT DEFAULT NULL
);

CREATE TABLE `partner_graphs` (
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `partner_id` INT DEFAULT NULL,
  `graph_id` INT DEFAULT NULL,
  `columns` INT DEFAULT NULL,
  `format` VARCHAR(255) DEFAULT NULL,
  `position` INT DEFAULT '0',
  `dashboard_id` INT NOT NULL DEFAULT '0'
);

CREATE TABLE `queries` (
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `unique_identifier` VARCHAR(25) NOT NULL UNIQUE,
  `query` TEXT NOT NULL
  `title` VARCHAR(50),  -- Add title column
  `description` TEXT    -- Add description column
);

CREATE TABLE `raw_malware` (
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `sample_id` INT NOT NULL,
  `sha1` VARCHAR(40) DEFAULT NULL UNIQUE,
  `filetype` VARCHAR(50) NOT NULL,
  `av_output_old` VARCHAR(255) DEFAULT NULL,
  `packer` VARCHAR(255) DEFAULT NULL,
  `av_output_family` VARCHAR(255) DEFAULT NULL,
  `av_output_id` INT DEFAULT NULL,
  `received_date` DATETIME DEFAULT NULL,
  `partner_id` INT DEFAULT NULL,
  `md5` VARCHAR(32) DEFAULT NULL,
  `analysis_status` VARCHAR(1) DEFAULT NULL,
  `ssdeep` VARCHAR(159) DEFAULT NULL,
  `analyzed` CHAR(1) DEFAULT NULL,
  `sent_to_partners` CHAR(1) DEFAULT NULL,
  `static_results_id` INT DEFAULT NULL
);

CREATE TABLE `report_descriptions` (
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL UNIQUE,
  `description` VARCHAR(255) NOT NULL
);

CREATE TABLE `schema_migrations` (
  `version` VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE `tabela1` (
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `title` VARCHAR(45) NOT NULL,
  `value` VARCHAR(45) NOT NULL
);

CREATE TABLE `user_partners` (
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `partner_id` INT NOT NULL
);

CREATE TABLE `users` (
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `login` VARCHAR(25) NOT NULL UNIQUE,
  `encrypted_password` VARCHAR(255) NOT NULL,
  `salt` VARCHAR(255) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `admin` INT NOT NULL DEFAULT '0'
);

CREATE TABLE user_queries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    query_id INT NOT NULL,
);

