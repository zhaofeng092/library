# -*- coding: utf-8 -*-
# @Time : 2021/3/9 9:46
# @公众号 : Python图书馆
# @File : game.py
# @Software: PyCharm
# @Description:下面代码用到了一些素材（游戏背景音乐、图片等等），可以到 https://www.itprojects.cn/detail.html?example_id=869a7cbfd9bd4d9b23e61a4d88e39b1c 下载，谢谢大家的支持


import random
import sys

import pygame

# 屏幕的宽、高
WIDTH = 630
HEIGHT = 630
# 边界值
BORDER_LEN = 3
# 字体
FONTPATH = 'resources/font/font.ttf'


class Iron(pygame.sprite.Sprite):
    """
    铁墙类
    """
    # 定义精灵组，将所有的砖墙实例对象添加到里面
    group = pygame.sprite.Group()

    def __init__(self, position):
        # 调用父类的初始化方法，这样才能够实现必要的初始化操作
        super().__init__()
        self.image = pygame.image.load("resources/images/scene/iron.png")
        # 当使用碰撞判断方法时，pygame就需要知道当前要检测的物体的位置，所以这个rect属性一定要设置
        self.rect = self.image.get_rect()
        self.rect.topleft = position

        # 添加到精灵组
        self.group.add(self)

    @classmethod
    def show(cls, screen):
        for temp in cls.group:
            screen.blit(temp.image, temp.rect)


class Ice(pygame.sprite.Sprite):
    """
    冰类
    """
    # 定义精灵组，将所有的实例对象添加到里面
    group = pygame.sprite.Group()

    def __init__(self, position):
        # 调用父类的初始化方法，这样才能够实现必要的初始化操作
        super().__init__()
        # 因为是12x12的小图片，所以需要制作一个24x24的image
        image = pygame.Surface((24, 24))
        for i in range(2):
            for j in range(2):
                image.blit(pygame.image.load("resources/images/scene/ice.png"), (12 * i, 12 * j))
        self.image = image
        # 当使用碰撞判断方法时，pygame就需要知道当前要检测的物体的位置，所以这个rect属性一定要设置
        self.rect = self.image.get_rect()
        self.rect.topleft = position

        # 添加到精灵组
        self.group.add(self)

    @classmethod
    def show(cls, screen):
        for temp in cls.group:
            screen.blit(temp.image, temp.rect)


class River(pygame.sprite.Sprite):
    """
    河流类
    """
    # 定义精灵组，将所有的实例对象添加到里面
    group = pygame.sprite.Group()

    def __init__(self, position):
        # 调用父类的初始化方法，这样才能够实现必要的初始化操作
        super().__init__()
        # 因为是12x12的小图片，所以需要制作一个24x24的image
        image = pygame.Surface((24, 24))
        for i in range(2):
            for j in range(2):
                image.blit(pygame.image.load("resources/images/scene/river1.png"), (12 * i, 12 * j))
        self.image = image
        # 当使用碰撞判断方法时，pygame就需要知道当前要检测的物体的位置，所以这个rect属性一定要设置
        self.rect = self.image.get_rect()
        self.rect.topleft = position

        # 添加到精灵组
        self.group.add(self)

    @classmethod
    def show(cls, screen):
        for temp in cls.group:
            screen.blit(temp.image, temp.rect)


class Tree(pygame.sprite.Sprite):
    """
    树类
    """
    # 定义精灵组，将所有的实例对象添加到里面
    group = pygame.sprite.Group()

    def __init__(self, position):
        # 调用父类的初始化方法，这样才能够实现必要的初始化操作
        super().__init__()
        # 因为是12x12的小图片，所以需要制作一个24x24的image
        image = pygame.Surface((24, 24))
        for i in range(2):
            for j in range(2):
                image.blit(pygame.image.load("resources/images/scene/tree.png"), (12 * i, 12 * j))
        self.image = image
        # 当使用碰撞判断方法时，pygame就需要知道当前要检测的物体的位置，所以这个rect属性一定要设置
        self.rect = self.image.get_rect()
        self.rect.topleft = position

        # 添加到精灵组
        self.group.add(self)

    @classmethod
    def show(cls, screen):
        for temp in cls.group:
            screen.blit(temp.image, temp.rect)


class Brick(pygame.sprite.Sprite):
    """
    砖墙类
    """

    # 定义精灵组，将所有的砖墙实例对象添加到里面
    group = pygame.sprite.Group()

    def __init__(self, position):
        # 调用父类的初始化方法，这样才能够实现必要的初始化操作
        super().__init__()
        self.image = pygame.image.load("resources/images/scene/brick.png")
        # 当使用碰撞判断方法时，pygame就需要知道当前要检测的物体的位置，所以这个rect属性一定要设置
        self.rect = self.image.get_rect()
        self.rect.topleft = position

        # 添加到精灵组
        self.group.add(self)

    @classmethod
    def show(cls, screen):
        for temp in cls.group:
            screen.blit(temp.image, temp.rect)


class Bullet(pygame.sprite.Sprite):
    """
    子弹类
    """
    # 定义精灵组，将所有的砖墙实例对象添加到里面
    group = pygame.sprite.Group()
    group_enemy = pygame.sprite.Group()

    def __init__(self, _type, direction, position):
        super().__init__()
        # 子弹图片
        if direction == "up":
            image_path = "resources/images/bullet/bullet_up.png"
        elif direction == "down":
            image_path = "resources/images/bullet/bullet_down.png"
        elif direction == "left":
            image_path = "resources/images/bullet/bullet_left.png"
        elif direction == "right":
            image_path = "resources/images/bullet/bullet_right.png"
        self.image = pygame.image.load(image_path)
        # 子弹位置
        self.rect = self.image.get_rect()
        self.rect.center = position  # 设置子弹的初始位置的中心点
        # 子弹方向
        self.direction = direction
        # 子弹移动速度
        self.speed = 8

        # 将子弹添加到精灵组
        if _type == "player":
            self.group.add(self)
        else:
            self.group_enemy.add(self)

    @classmethod
    def auto_move(cls):
        for temp in cls.group:
            if temp.rect.x < BORDER_LEN or temp.rect.x > WIDTH - BORDER_LEN or temp.rect.y < BORDER_LEN or temp.rect.y > HEIGHT - BORDER_LEN:
                cls.group.remove(temp)
                print("子弹超出边界，移除子弹")
                continue

            if temp.direction == "up":
                temp.rect = temp.rect.move((0, -temp.speed))
            elif temp.direction == "down":
                temp.rect = temp.rect.move((0, temp.speed))
            elif temp.direction == "left":
                temp.rect = temp.rect.move((-temp.speed, 0))
            elif temp.direction == "right":
                temp.rect = temp.rect.move((temp.speed, 0))

        for temp in cls.group_enemy:
            if temp.rect.x < BORDER_LEN or temp.rect.x > WIDTH - BORDER_LEN or temp.rect.y < BORDER_LEN or temp.rect.y > HEIGHT - BORDER_LEN:
                cls.group_enemy.remove(temp)
                print("子弹超出边界，移除子弹")
                continue

            if temp.direction == "up":
                temp.rect = temp.rect.move((0, -temp.speed))
            elif temp.direction == "down":
                temp.rect = temp.rect.move((0, temp.speed))
            elif temp.direction == "left":
                temp.rect = temp.rect.move((-temp.speed, 0))
            elif temp.direction == "right":
                temp.rect = temp.rect.move((temp.speed, 0))

        # 子弹碰砖墙(如果相碰，那么就移除当前子弹以及砖墙)
        pygame.sprite.groupcollide(cls.group, Brick.group, True, True)
        pygame.sprite.groupcollide(cls.group_enemy, Brick.group, True, True)
        # 子弹碰铁墙(如果相碰，那么只移除子弹)
        for bullet in cls.group:
            if pygame.sprite.spritecollide(bullet, Iron.group, False, None):
                cls.group.remove(bullet)
        for bullet in cls.group_enemy:
            if pygame.sprite.spritecollide(bullet, Iron.group, False, None):
                cls.group_enemy.remove(bullet)

    @classmethod
    def show(cls, screen):
        """
        显示子弹
        """
        for temp in cls.group:
            screen.blit(temp.image, temp.rect)

        for temp in cls.group_enemy:
            screen.blit(temp.image, temp.rect)

    @classmethod
    def move_and_show(cls, screen):
        """
        移动、显示子弹
        """
        cls.auto_move()
        cls.show(screen)


class PlayerTank(pygame.sprite.Sprite):
    """
    我方坦克类
    """
    # 定义类属性，存储我方坦克（如果是单人模式就只有1个，如果是双人模式就有2个）
    player_group = list()
    # 定义精灵组，用来碰撞等判断
    group = pygame.sprite.Group()

    def __init__(self, player, top_left):
        """
        实现初始化功能
        """
        # 调用父类的初始化方法，这样才能够实现必要的初始化操作
        super().__init__()
        # 坦克的图片
        image_path = "resources/images/playerTank/tank_T1_0.png" if player == "player1" else "resources/images/playerTank/tank_T2_0.png"
        self.tank_all_image = pygame.image.load(image_path).convert_alpha()
        self.image = self.tank_all_image.subsurface((0, 0), (48, 48))
        # 当使用碰撞判断方法时，pygame就需要知道当前要检测的物体的位置，所以这个rect属性一定要设置
        self.rect = self.image.get_rect()
        self.rect.topleft = top_left
        # 记录初始位置，以便在被击中后能够重新在默认位置出现
        self.origin_position = top_left
        # 定义移动的步长
        self.step_length = 8
        # 坦克的默认方向
        self.direction = "up"  # 默认朝上
        # 移动缓冲, 用于避免坦克连续移动过快导致不方便调整位置
        self.move_cache_time = 4
        self.move_cache_count = 0
        # 坦克轮子转动效果
        self.switch_count = 0
        self.switch_time = 2
        self.switch_image_index = False
        self.image_postion_index = 0
        # 发射子弹的间隔
        self.is_bullet_cooling = False  # 如果是第一次发射子弹，则不在冷却时间内，可以正常发射
        self.bullet_cooling_count = 0
        self.bullet_cooling_time = 30
        # 我方坦克生命次数
        self.life_num = 3
        # 标记此坦克是否显示
        self.is_show_flag = True

        # 将当前对象添加到类属性中，这样就可以通过类对象访问到我方坦克
        self.__class__.player_group.append(self)  # 或者self.player_group.append(self)也是可以的
        # 添加到精灵组
        self.group.add(self)

    def update_direction(self):
        """
        更新坦克的朝向
        """
        if self.direction == 'up':
            self.image = self.tank_all_image.subsurface((0, 0), (48, 48))
            self.image_postion_index = 0
        elif self.direction == 'down':
            self.image = self.tank_all_image.subsurface((0, 48), (48, 48))
            self.image_postion_index = 48
        elif self.direction == 'left':
            self.image = self.tank_all_image.subsurface((0, 96), (48, 48))
            self.image_postion_index = 96
        elif self.direction == 'right':
            self.image = self.tank_all_image.subsurface((0, 144), (48, 48))
            self.image_postion_index = 144

    def move(self, direction, group_list):
        """
        根据键盘调整坦克方向，然后移动
        """
        # 如果要移动的方向与当前坦克的朝向不同，则先调整朝向
        if self.direction != direction:
            self.direction = direction
            self.update_direction()
            return

        # 移动缓冲
        self.move_cache_count += 1
        if self.move_cache_count < self.move_cache_time:
            return
        else:
            self.move_cache_count = 0

        # 移动坦克
        # 复制一份当前玩家坦克的坐标，如果碰到障碍物之后，可以进行恢复
        rect_ori = self.rect
        if direction == "up":
            self.rect = self.rect.move((0, -self.step_length))
        elif direction == "down":
            self.rect = self.rect.move((0, self.step_length))
        elif direction == "left":
            self.rect = self.rect.move((-self.step_length, 0))
        elif direction == "right":
            self.rect = self.rect.move((self.step_length, 0))
        # 检测碰撞"砖墙"、"铁墙"、"冰"、"河流"。"树"无需检查
        for group in group_list:
            if pygame.sprite.spritecollide(self, group, False, None):
                self.rect = rect_ori

        # 判断碰撞到边界
        if self.rect.top < BORDER_LEN:
            self.rect.top = BORDER_LEN
        elif self.rect.bottom > HEIGHT - BORDER_LEN:
            self.rect.bottom = HEIGHT - BORDER_LEN
        elif self.rect.left < BORDER_LEN:
            self.rect.left = BORDER_LEN
        elif self.rect.right > WIDTH - BORDER_LEN:
            self.rect.right = WIDTH - BORDER_LEN

        # 为坦克轮动特效切换图片
        self.switch_count += 1
        if self.switch_count > self.switch_time:
            self.switch_count = 0
            self.switch_image_index = not self.switch_image_index
            self.image = self.tank_all_image.subsurface((48 * int(self.switch_image_index), self.image_postion_index),
                                                        (48, 48))

    def fire(self):
        """
        发射子弹
        """
        if not self.is_bullet_cooling:
            if self.direction == "up":
                position = (self.rect.centerx, self.rect.y)
            elif self.direction == "down":
                position = (self.rect.centerx, self.rect.y + 48)
            elif self.direction == "left":
                position = (self.rect.x, self.rect.centery)
            elif self.direction == "right":
                position = (self.rect.x + 48, self.rect.centery)
            Bullet("player", self.direction, position)
            print("我方坦克发射子弹")

    @classmethod
    def move_player_tank(cls, is_dual_mode, group_list):
        """
        控制我方坦克移动
        """
        # 检查用户按键，从而控制坦克移动
        key_pressed = pygame.key.get_pressed()

        # 定义移动的步长
        step_length = 8

        # 复制一份当前玩家1的坐标，如果碰到障碍物之后，可以进行恢复
        # rect_ori = cls.player_group[0].rect
        # 玩家一, ASWD移动
        if key_pressed[pygame.K_w]:
            cls.player_group[0].move("up", group_list)
        elif key_pressed[pygame.K_s]:
            cls.player_group[0].move("down", group_list)
        elif key_pressed[pygame.K_a]:
            cls.player_group[0].move("left", group_list)
        elif key_pressed[pygame.K_d]:
            cls.player_group[0].move("right", group_list)
        elif key_pressed[pygame.K_SPACE]:
            # 如果按下了空格键，那么就发射子弹
            cls.player_group[0].fire()

        # 检查玩家1是否碰撞到障碍物
        # # 检测碰撞"砖墙"
        # if pygame.sprite.spritecollide(cls.player_group[0], brick_group, False, None):
        #     print("玩家1碰到了砖墙", cls.player_group[0].rect)
        #     cls.player_group[0].rect = rect_ori

        # 玩家二, ↑↓←→移动
        if is_dual_mode:
            # 复制一份当前玩家2的坐标，如果碰到障碍物之后，可以进行恢复
            # rect_ori = cls.player_group[1].rect
            if key_pressed[pygame.K_UP]:
                cls.player_group[1].move("up", group_list)
            elif key_pressed[pygame.K_DOWN]:
                cls.player_group[1].move("down", group_list)
            elif key_pressed[pygame.K_LEFT]:
                cls.player_group[1].move("left", group_list)
            elif key_pressed[pygame.K_RIGHT]:
                cls.player_group[1].move("right", group_list)
            elif key_pressed[pygame.K_KP0]:
                # 如果按下了数字0，那么就发射子弹
                cls.player_group[1].fire()

            # 检查玩家2是否碰撞到障碍物
            # 检测碰撞"砖墙"
            # if pygame.sprite.spritecollide(cls.player_group[1], brick_group, False, None):
            #     cls.player_group[1].rect = rect_ori

    def bullet_cooling(self):
        """
        判断发射子弹的冷却时间是否达到
        """
        # 对发射子弹的冷却时间计数
        self.bullet_cooling_count += 1
        if self.bullet_cooling_count > self.bullet_cooling_time:
            self.is_bullet_cooling = False  # 不在冷却状态，即意味着可以发射子弹
            self.bullet_cooling_count = 0
            print("冷却完毕...")
        else:
            self.is_bullet_cooling = True  # 不能发射，正在冷却

    def judge_bomb(self):
        """
        判断是否被击中
        """
        # 判断碰撞到敌方坦克子弹
        if pygame.sprite.spritecollide(self, Bullet.group_enemy, True, None):
            self.life_num -= 1  # 如果被击中，那么就生命值-1
            if self.life_num == 0:
                self.is_show_flag = False  # 如果已经没有了生命值，那么就标记为不显示
            # 重新设置位置为初始位置
            self.rect.topleft = self.origin_position

    @classmethod
    def show(cls, screen, is_dual_mode):
        """
        显示我方坦克
        """
        if cls.player_group:
            if cls.player_group[0].is_show_flag:
                screen.blit(cls.player_group[0].image, cls.player_group[0].rect)
                # 对发射子弹的冷却时间计数
                cls.player_group[0].bullet_cooling()
                # 判断是否被击中
                cls.player_group[0].judge_bomb()
            if is_dual_mode and cls.player_group[1].is_show_flag:
                # 如果是双人模式
                screen.blit(cls.player_group[1].image, cls.player_group[1].rect)
                # 对发射子弹的冷却时间计数
                cls.player_group[1].bullet_cooling()
                # 判断是否被击中
                cls.player_group[1].judge_bomb()


class PlayerHome(pygame.sprite.Sprite):
    """
    我方大本营
    """
    home = None

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("resources/images/home/home1.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.__class__.home = self

    @classmethod
    def show(cls, screen):
        """
        显示大本营
        """
        screen.blit(cls.home.image, cls.home.rect)


class EnemyTank(pygame.sprite.Sprite):
    """
    敌人坦克类
    """
    # 定义精灵组，将所有的实例对象添加到里面
    group = pygame.sprite.Group()

    def __init__(self, position):
        # 调用父类的初始化方法，这样才能够实现必要的初始化操作
        super().__init__()
        # 坦克默认的朝向
        self.direction = random.choice(["up", "down", "left", "right"])
        self.tank_all_image = pygame.image.load("resources/images/enemyTank/enemy_1_0.png")
        self.image = None
        self.update_direction()  # 根据随机朝向，计算出要使用的坦克图片
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        # 坦克默认的速度
        self.speed = random.choice([2, 4])
        # 发射子弹的间隔
        self.is_bullet_cooling = True
        self.bullet_cooling_count = 0
        self.bullet_cooling_time = 5

        # 添加到精灵组
        self.group.add(self)

    def update_direction(self):
        """
        更新坦克的朝向
        """
        if self.direction == 'up':
            self.image = self.tank_all_image.subsurface((0, 0), (48, 48))
        elif self.direction == 'down':
            self.image = self.tank_all_image.subsurface((0, 48), (48, 48))
        elif self.direction == 'left':
            self.image = self.tank_all_image.subsurface((0, 96), (48, 48))
        elif self.direction == 'right':
            self.image = self.tank_all_image.subsurface((0, 144), (48, 48))

    @classmethod
    def show(cls, screen):
        for temp in cls.group:
            screen.blit(temp.image, temp.rect)

    def move(self, group_list):
        """
        敌方坦克自动移动
        :return:
        """

        # 记录位置，以便在碰到障碍物之后，能够恢复
        rect_ori = self.rect
        if self.direction == "up":
            self.rect = self.rect.move((0, -self.speed))
        elif self.direction == "down":
            self.rect = self.rect.move((0, self.speed))
        elif self.direction == "left":
            self.rect = self.rect.move((-self.speed, 0))
        elif self.direction == "right":
            self.rect = self.rect.move((self.speed, 0))

        # 检测碰撞"砖墙"、"铁墙"、"冰"、"河流"。"树"无需检查
        for group in group_list:
            if pygame.sprite.spritecollide(self, group, False, None):
                self.rect = rect_ori
                # 随机得到新的朝向
                self.direction = random.choice(["up", "down", "left", "right"])
                self.update_direction()

        # 碰撞到其他敌方坦克
        # 先将本坦克从精灵组中移除
        self.group.remove(self)
        # 然后再判断是否碰撞到其他敌方坦克
        if pygame.sprite.spritecollide(self, self.group, False, None):
            self.rect = rect_ori
            # 随机得到新的朝向
            self.direction = random.choice(["up", "down", "left", "right"])
            self.update_direction()
        # 判断之后再将本坦克添加到精灵组
        self.group.add(self)

        # 碰撞到玩家坦克
        if pygame.sprite.spritecollide(self, PlayerTank.group, False, None):
            self.rect = rect_ori
            # 随机得到新的朝向
            self.direction = random.choice(["up", "down", "left", "right"])
            self.update_direction()

        # 碰撞到我方子弹
        if pygame.sprite.spritecollide(self, Bullet.group, True, None):
            self.group.remove(self)

        # 判断碰撞到边界，然后再次随机新朝向
        if self.rect.top < BORDER_LEN:
            self.rect.top = BORDER_LEN
            # 随机得到新的朝向
            self.direction = random.choice(["up", "down", "left", "right"])
            self.update_direction()
        elif self.rect.bottom > HEIGHT - BORDER_LEN:
            self.rect.bottom = HEIGHT - BORDER_LEN
            # 随机得到新的朝向
            self.direction = random.choice(["up", "down", "left", "right"])
            self.update_direction()
        elif self.rect.left < BORDER_LEN:
            self.rect.left = BORDER_LEN
            # 随机得到新的朝向
            self.direction = random.choice(["up", "down", "left", "right"])
            self.update_direction()
        elif self.rect.right > WIDTH - BORDER_LEN:
            self.rect.right = WIDTH - BORDER_LEN
            # 随机得到新的朝向
            self.direction = random.choice(["up", "down", "left", "right"])
            self.update_direction()

    @classmethod
    def auto_move(cls, group_list):
        for temp in cls.group:
            temp.move(group_list)

    @classmethod
    def auto_move_and_show(cls, screen, group_list):
        cls.auto_move(group_list)
        cls.show(screen)

    def judge_cooling_and_fire(self):
        """
        判断是否达到冷却时间（即发射子弹要有间隔），然后发射
        """
        self.bullet_cooling_count += 1
        if self.bullet_cooling_count > self.bullet_cooling_time:
            self.bullet_cooling_count = 0
            if random.randint(1, 10) == 6:  # 如果随机得到的数字恰巧是6，那么就表示冷却时间到
                self.is_bullet_cooling = False

        if not self.is_bullet_cooling:
            # 创建子弹对象
            if self.direction == "up":
                position = (self.rect.centerx, self.rect.y)
            elif self.direction == "down":
                position = (self.rect.centerx, self.rect.y + 48)
            elif self.direction == "left":
                position = (self.rect.x, self.rect.centery)
            elif self.direction == "right":
                position = (self.rect.x + 48, self.rect.centery)
            Bullet("enemy", self.direction, position)

        # 发射完毕后，立刻设置为冷却状态
        self.is_bullet_cooling = True

    @classmethod
    def fire(cls):
        """
        发射子弹
        """
        for temp in cls.group:
            temp.judge_cooling_and_fire()


class Game(object):
    """
    游戏控制类
    """

    def __init__(self):
        """
        初始化工作
        """
        # 游戏初始化
        pygame.init()
        # 创建用来显示画面的对象（理解为相框）
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def game_start_interface(self):
        """
        显示游戏开始画面（让用户选择游戏人数）
        :return:False为单人模式，True为双人模式
        """
        # 准备用到的图片
        background_img = pygame.image.load("resources/images/others/background.png")
        logo_img = pygame.image.load("resources/images/others/logo.png")
        logo_img = pygame.transform.scale(logo_img, (446, 70))  # 图片缩小1倍，即将892x140-->446x70
        logo_rect = logo_img.get_rect()  # 得到这个图片的左上角的坐标（默认是（0,0)点），以及宽高
        # 为了能够让logo图片在合适的位置显示，我们可以设置它的中心点的坐标，它会根据自身的宽高自动计算出左上角的坐标
        logo_rect.centerx, logo_rect.centery = WIDTH / 2, HEIGHT // 4
        # print(logo_rect.topleft)  # 在终端中看到，此时输出的值是：(92, 122)

        # 准备要显示文本（1player、2players）
        # 字体
        font = pygame.font.Font(FONTPATH, 60)  # 60表示要显示的字体大小
        font_color_white = (255, 255, 255)  # 要显示的字体颜色为白色
        # 1player
        one_player_text = font.render('1 PLAYER', True, font_color_white)
        one_player_rect = one_player_text.get_rect()
        one_player_rect.left, one_player_rect.top = WIDTH / 2 - 50, HEIGHT / 2 - 60
        # 2players
        two_players_text = font.render('2 PLAYERS', True, font_color_white)
        two_players_rect = two_players_text.get_rect()
        two_players_rect.left, two_players_rect.top = WIDTH / 2 - 50, HEIGHT / 2

        # 游戏人数选择时的图片
        select_player_num_tank = pygame.image.load(
            "resources/images/playerTank/tank_T1_0.png").convert_alpha().subsurface((0, 144), (48, 48))
        select_player_num_tank_rect = select_player_num_tank.get_rect()

        # 游戏开始提示
        game_tip = font.render('press <Enter> to start', True, font_color_white)
        game_tip_rect = game_tip.get_rect()
        game_tip_rect.centerx, game_tip_rect.top = WIDTH / 2, HEIGHT / 1.4

        # 创建一个计时器，用来实现更加方便的延时（防止while循环过快，占用太多CPU的问题）
        clock = pygame.time.Clock()

        # 存储游戏人数（False单人，True双人）
        is_dual_mode = False

        # 主循环
        while True:
            # 事件检测（例如点击了键盘、鼠标点击等）
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 如果用鼠标点击了:x:，那么就退出程序
                    pygame.quit()
                    sys.exit()  # 退出程序
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return is_dual_mode
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                        is_dual_mode = not is_dual_mode
                        # print("当前选择的游戏人数是（True双人、False单人）", is_dual_mode)

            # 从(0,0)点（即左上角）开始贴一张图片（理解为在screen这个相框中从左上角开始贴一张照片）
            self.screen.blit(background_img, (0, 0))

            # 显示logo
            self.screen.blit(logo_img, logo_rect)

            # 显示游戏人数文字
            self.screen.blit(one_player_text, one_player_rect)
            self.screen.blit(two_players_text, two_players_rect)
            # 显示标记选择的人数的tank
            if is_dual_mode:
                # 双人模式
                select_player_num_tank_rect.right, select_player_num_tank_rect.top = two_players_rect.left - 10, two_players_rect.top
                self.screen.blit(select_player_num_tank, select_player_num_tank_rect)
            else:
                # 单人模式
                select_player_num_tank_rect.right, select_player_num_tank_rect.top = one_player_rect.left - 10, one_player_rect.top
                self.screen.blit(select_player_num_tank, select_player_num_tank_rect)

            # 显示提示
            self.screen.blit(game_tip, game_tip_rect)

            # 显示screen这个相框的内容（此时在这个相框中的内容像照片、文字等会显示出来）
            pygame.display.update()

            # FPS（每秒钟显示画面的次数）
            clock.tick(60)  # 通过一定的延时，实现1秒钟能够循环60次

    def game_end_interface(self, is_win):
        """
        显示游戏结束画面
        """
        # 背景
        background_img = pygame.image.load("resources/images/others/background.png")

        # 游戏失败图
        game_over_img = pygame.image.load("resources/images/others/gameover.png")
        game_over_img = pygame.transform.scale(game_over_img, (150, 75))
        game_over_img_rect = game_over_img.get_rect()
        game_over_img_rect.midtop = WIDTH / 2, HEIGHT / 8

        # 游戏胜利、失败字体
        color_white = (255, 255, 255)
        font = pygame.font.Font(FONTPATH, 60)
        # 游戏胜利与否的提示
        if is_win:
            font_render = font.render('Congratulations, You win!', True, color_white)
        else:
            font_render = font.render('Sorry, You fail!', True, color_white)
        font_rect = font_render.get_rect()
        font_rect.centerx, font_rect.centery = WIDTH / 2, HEIGHT / 3

        # 用于选择退出或重新开始
        # 用于选择的坦克光标
        tank_cursor = pygame.image.load("resources/images/playerTank/tank_T1_0.png").convert_alpha().subsurface(
            (0, 144), (48, 48))
        tank_rect = tank_cursor.get_rect()
        # 重新运行
        restart_render_white = font.render('RESTART', True, color_white)
        restart_rect = restart_render_white.get_rect()
        restart_rect.left, restart_rect.top = WIDTH / 2.4, HEIGHT / 2
        # 退出
        quit_render_white = font.render('QUIT', True, color_white)
        quit_rect = quit_render_white.get_rect()
        quit_rect.left, quit_rect.top = WIDTH / 2.4, HEIGHT / 1.6

        # 标记当前选择的是退出还是继续游戏
        is_quit_game = False

        # 创建计时器对象，用于控制刷新频率
        clock = pygame.time.Clock()

        # 主循环
        while True:
            # 检查键盘事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return is_quit_game
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                        is_quit_game = not is_quit_game

            # 显示背景
            self.screen.blit(background_img, (0, 0))
            self.screen.blit(game_over_img, game_over_img_rect)
            self.screen.blit(font_render, font_rect)

            if not is_quit_game:
                tank_rect.right, tank_rect.top = restart_rect.left - 10, restart_rect.top
                self.screen.blit(tank_cursor, tank_rect)
                self.screen.blit(quit_render_white, quit_rect)
                self.screen.blit(restart_render_white, restart_rect)
            else:
                tank_rect.right, tank_rect.top = quit_rect.left - 10, quit_rect.top
                self.screen.blit(tank_cursor, tank_rect)
                self.screen.blit(quit_render_white, quit_rect)
                self.screen.blit(restart_render_white, restart_rect)

            # 刷新显示画面，此时才会真正的显示
            pygame.display.update()

            # 控制频率，FPS为60，每秒钟60次刷新
            clock.tick(60)

    def parse_game_level_file(self):
        """
        解析关卡文件
        """
        # 每个地图元素占用的像素（配置文件，例如1.lvl中注释里说明了Grid SIZE: 24 * 24 pixels）
        grid_size = 24
        # 定义大本营
        # home_dict = dict()

        with open("./levels/3.lvl", errors='ignore') as f:
            num_row = -1  # 用来标记地图元素是整个地图的第几行（总共26行，26列）
            for line in f.readlines():
                line = line.strip('\n')  # 切除每行行尾的换行符
                # 如果当前要处理的行是地图元素，那么就继续处理
                if line[0] in ["S", "B", "I", "R", "C", "T"]:
                    # 地图元素
                    num_row += 1
                    # print("当前是第%d行" % num_row)
                    for num_col, elem in enumerate(line.split(' ')):
                        # print("当前是第%d行，第%d列" % (num_row, num_col))
                        position = BORDER_LEN + num_col * grid_size, BORDER_LEN + num_row * grid_size
                        if elem == 'B':
                            # 创建砖墙对象，然后添加到精灵组
                            Brick(position)
                        elif elem == 'I':
                            # 创建铁墙对象，然后添加到精灵组
                            Iron(position)
                        elif elem == 'R':
                            # 创建河流对象，然后添加到精灵组
                            River(position)
                        elif elem == 'C':
                            # 创建冰对象，然后添加到精灵组
                            Ice(position)
                        elif elem == 'T':
                            # 创建树对象，然后添加到精灵组
                            Tree(position)
                elif line.startswith('%HOMEPOS'):
                    # 大本营位置
                    home_position = line.split(':')[-1]
                    home_position = int(home_position.split(',')[0]), int(home_position.split(',')[1])
                    home_position = (
                    BORDER_LEN + home_position[0] * grid_size, BORDER_LEN + home_position[1] * grid_size)
                    # 创建大本营类
                    PlayerHome(home_position)
                elif line.startswith('%PLAYERTANKPOS'):
                    # 我方坦克初始位置
                    player_tank_positions = line.split(':')[-1]
                    player_tank_positions = [(int(pos.split(',')[0]), int(pos.split(',')[1])) for pos in
                                             player_tank_positions.split(' ')]
                    player_tank_positions = [[BORDER_LEN + pos[0] * grid_size, BORDER_LEN + pos[1] * grid_size] for pos
                                             in player_tank_positions]

                    # 从这个图片中切除一部分来当做要使用的图片，即玩家1的坦克
                    # image = pygame.image.load("resources/images/playerTank/tank_T1_0.png").convert_alpha()
                    # image = image.subsurface((0, 0), (48, 48))
                    # player1_dict = {
                    #     "image": image,
                    #     "top_left": player_tank_positions[0]
                    # }

                    # 创建我方玩家1的坦克，然后添加到列表中
                    PlayerTank("player1", player_tank_positions[0])

                    # 从这个图片中切除一部分来当做要使用的图片，即玩家2的坦克
                    # image = pygame.image.load("resources/images/playerTank/tank_T2_0.png").convert_alpha()
                    # image = image.subsurface((0, 0), (48, 48))
                    # player2_dict = {
                    #     "image": image,
                    #     "top_left": player_tank_positions[1]
                    # }
                    # player_group.append(player1_dict)
                    # player_group.append(player2_dict)

                    # 创建我方玩家2的坦克，然后添加到列表中
                    PlayerTank("player2", player_tank_positions[1])
                elif line.startswith('%ENEMYTANKPOS'):
                    # 敌方坦克初始位置
                    position = line.split(':')[-1]
                    position = [[int(pos.split(',')[0]), int(pos.split(',')[1])] for pos in position.split(' ')]
                    position = [(BORDER_LEN + pos[0] * grid_size, BORDER_LEN + pos[1] * grid_size) for pos in position]
                    # 根据敌方坦克的初始位置创建多个坦克
                    for pos in position:
                        EnemyTank(pos)

    def game_run_level(self, is_dual_mode):
        """
        运行游戏
        """
        # 背景图片
        background_img = pygame.image.load("resources/images/others/background.png")

        # 调用解析关卡配置文件
        self.parse_game_level_file()

        # 帧率控制对象
        clock = pygame.time.Clock()

        # 运行游戏的主循环
        is_win = False
        is_running = True
        while is_running:
            # 事件检测（例如点击了键盘、鼠标点击等）
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # 通过键盘控制坦克移动
            PlayerTank.move_player_tank(is_dual_mode, [Brick.group, River.group, Ice.group, Iron.group])

            # 敌方坦克开发
            EnemyTank.fire()

            # 碰撞检测
            # 子弹碰大本营（无论是我方还是敌方子弹，只要碰到都认为本关卡游戏结束）
            if pygame.sprite.spritecollide(PlayerHome.home, Bullet.group, True, None) or pygame.sprite.spritecollide(
                    PlayerHome.home, Bullet.group_enemy, True, None):
                is_running = False  # 如果碰撞到大本营，那么通过修改这个变量为False让while循环结束，游戏即将结束运行
                is_win = False

            # 如果敌方坦克没有了，则认为我方胜利
            if len(EnemyTank.group) == 0:
                is_running = False
                is_win = True

            # 如果我方坦克没有了生命值，则认为游戏输了
            if (not is_dual_mode and PlayerTank.player_group[0].life_num == 0) or \
                    (is_dual_mode and PlayerTank.player_group[0].life_num == 0 and PlayerTank.player_group[
                        1].life_num == 0):
                is_running = False
                is_win = False

            # 显示游戏背景
            self.screen.blit(background_img, (0, 0))
            # 显示砖墙
            Brick.show(self.screen)
            # 显示铁墙
            Iron.show(self.screen)
            # 显示河流
            River.show(self.screen)
            # 显示冰
            Ice.show(self.screen)
            # 显示树
            Tree.show(self.screen)

            # 显示大本营
            PlayerHome.show(self.screen)

            # 显示我方坦克
            PlayerTank.show(self.screen, is_dual_mode)

            # 显示我方坦克发射的子弹
            Bullet.move_and_show(self.screen)

            # 显示敌方坦克
            EnemyTank.auto_move_and_show(self.screen, [Brick.group, River.group, Ice.group, Iron.group])

            # 刷新要显示的内容，从而真正的显示
            pygame.display.update()
            # 每秒钟控制为60帧
            clock.tick(60)

        return is_win

    def clean(self):
        """
        清理上一次游戏留下的残留
        """
        EnemyTank.group.empty()
        PlayerTank.group.empty()
        PlayerTank.player_group.clear()
        Brick.group.empty()
        Ice.group.empty()
        River.group.empty()
        Iron.group.empty()
        Tree.group.empty()
        Bullet.group.empty()
        Bullet.group_enemy.empty()

    def run(self):
        # 显示游戏开始画面，让用户选择游戏人数
        is_dual_mode = self.game_start_interface()
        # 调用游戏关卡函数，从而开始游戏
        is_win = self.game_run_level(is_dual_mode)
        # 接下来根据is_win来显示对应的输赢界面
        while True:
            if self.game_end_interface(is_win):  # 如果返回为True，那么就意味着退出游戏，否则继续游戏
                break

            # 继续重新游戏
            # 清理上一次游戏的残留
            self.clean()
            # 创建用来显示画面的对象（理解为相框）
            pygame.display.set_mode((WIDTH, HEIGHT))
            # 显示游戏开始画面，让用户选择游戏人数
            is_dual_mode = self.game_start_interface()
            # 调用游戏关卡函数，从而开始游戏
            is_win = self.game_run_level(is_dual_mode)


if __name__ == '__main__':
    """
    整体流程的控制
    """
    game = Game()
    game.run()
