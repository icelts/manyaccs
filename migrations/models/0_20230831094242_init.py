from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `kami` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `type` INT NOT NULL  COMMENT 'product id',
    `kamicontent` LONGTEXT NOT NULL  COMMENT '卡密内容',
    `status` INT NOT NULL  COMMENT '卡密状态，1为未出售' DEFAULT 1,
    `creatted` DATETIME(6) NOT NULL  COMMENT '卡密创建时间',
    `soldtime` DATETIME(6) NOT NULL  COMMENT '售出时间'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `orders` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `ordercontent` LONGTEXT NOT NULL,
    `productid` LONGTEXT NOT NULL,
    `userids` LONGTEXT NOT NULL  COMMENT '购买用户ID',
    `charged` DOUBLE NOT NULL  COMMENT '订单扣款',
    `ordertime` DATETIME(6) NOT NULL  COMMENT '售出时间'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `products` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` LONGTEXT NOT NULL  COMMENT '商品名字',
    `jianjie` LONGTEXT NOT NULL  COMMENT '商品描述'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `token` VARCHAR(32) NOT NULL  COMMENT '用户的token',
    `balance` INT NOT NULL  COMMENT '余额' DEFAULT 0,
    `status` INT NOT NULL  COMMENT '用户状态，1为激活状态' DEFAULT 1,
    `lastactive` DATETIME(6) NOT NULL,
    `creattime` DATETIME(6) NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
