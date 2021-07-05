from random import randint
from math import radians, sin, cos, sqrt, floor


def output(filename, rooms):
    file_output = 'versioninfo\n{\n}\nvisgroups\n{\n}\n'
    file_output += 'viewsettings\n{\n"bSnapToGrid" "1"\n"bShowGrid" "1"\n"bShowLogicalGrid" "0"\n"nGridSpacing" "16"\n"bShow3DGrid" "0"\n}\n'
    file_output += 'world\n{\n"id" "1"\n"mapversion" "1"\n"classname" "worldspawn"\n"skyname" "sky_day01_01"\n"maxpropscreenwidth" "-1"\n"detailvbsp" "detail.vbsp"\n"detailmaterial" "detail/detailsprites"\n'

    # add brushes
    for room in rooms:
        for wall in room.walls():
            file_output += wall
    file_output += '\n}\n'

    # add instances
    for inst in instances:
        file_output += str(inst)

    with open(filename, "w+") as f:
        f.write(file_output)

    print(filename)


def side(id, a, b, c, u, v, tex='TOOLS/TOOLSNODRAW'):
    text = 'side\n{\n'
    text += '"id" "' + str(id) + '"\n'
    text += '"plane" "('+str(a[0])+' '+str(a[1])+' '+str(a[2])+') ' \
            '('+str(b[0])+' '+str(b[1])+' '+str(b[2])+') ' \
            '('+str(c[0])+' '+str(c[1])+' '+str(c[2])+')"\n'
    text += '"material" "' + tex + '"\n'
    text += '"uaxis" "['+str(u[0])+' '+str(u[1])+' '+str(u[2])+' '+str(u[3])+'] 0.25"\n'
    text += '"vaxis" "['+str(v[0])+' '+str(v[1])+' '+str(v[2])+' '+str(v[3])+'] 0.25"\n'
    text += '"rotation" "0"\n'
    text += '"lightmapscale" "16"\n'
    text += '"smoothing_groups" "0"\n'
    text += '}\n'
    return text


def solid_cube(x1, y1, x2, y2, z1, z2):
    global solid_count

    solid_count += 1
    id = solid_count
    sid = (id-2)*6

    text = 'solid\n{\n"id" "' + str(id) + '"\n'
    text += side(sid + 1, (x1, y2, z2), (x2, y2, z2), (x2, y1, z2), (1, 0, 0, 0), (0, -1, 0, 0))   # top
    text += side(sid + 2, (x1, y1, z1), (x2, y1, z1), (x2, y2, z1), (-1, 0, 0, 0), (0, -1, 0, 0))   # bottom
    text += side(sid + 3, (x1, y2, z2), (x1, y1, z2), (x1, y1, z1), (0, -1, 0, 0), (0, 0, -1, 0))   # west (left)
    text += side(sid + 4, (x2, y2, z1), (x2, y1, z1), (x2, y1, z2), (0, 1, 0, 0), (0, 0, -1, 0))   # east (right)
    text += side(sid + 5, (x2, y2, z2), (x1, y2, z2), (x1, y2, z1), (-1, 0, 0, 0), (0, 0, -1, 0))   # north (top)
    text += side(sid + 6, (x2, y1, z1), (x1, y1, z1), (x1, y1, z2), (1, 0, 0, 0), (0, 0, -1, 0))   # south (bottom)
    text += 'editor\n{\n"color" "0 ' + str(randint(100, 210)) + ' ' + str(
        randint(100, 210)) + '"\n"visgroupshown" "1"\n"visgroupautoshown" "1"\n}\n}\n'
    return text

def solid_floor(x1, y1, x2, y2, z):
    global solid_count

    solid_count += 1
    id = solid_count
    sid = (id - 2) * 6

    text = 'solid\n{\n"id" "' + str(id) + '"\n'
    text += side(sid + 1, (x1, y1, z), (x1, y2, z), (x2, y2, z), (1, 0, 0, 0), (0, -1, 0, 0), 'DEV/DEV_MEASUREGENERIC01B')   # top
    text += side(sid + 2, (x1+16, y2-16, z-16), (x1+16, y1+16, z-16), (x2-16, y1+16, z-16), (-1, 0, 0, 0), (0, -1, 0, 0))   # bottom
    text += side(sid + 3, (x1+16, y1+16, z-16), (x1+16, y2-16, z-16), (x1, y2, z), (0, -1, 0, 0), (0, 0, -1, 0))   # west (left)
    text += side(sid + 4, (x2-16, y2-16, z-16), (x2-16, y1+16, z-16), (x2, y1, z), (0, 1, 0, 0), (0, 0, -1, 0))   # east (right)
    text += side(sid + 5, (x1+16, y2-16, z-16), (x2-16, y2-16, z-16), (x2, y2, z), (-1, 0, 0, 0), (0, 0, -1, 0))   # north (top)
    text += side(sid + 6, (x2-16, y1+16, z-16), (x1+16, y1+16, z-16), (x1, y1, z), (1, 0, 0, 0), (0, 0, -1, 0))   # south (bottom)
    text += 'editor\n{\n"color" "0 ' + str(randint(100, 210)) + ' ' + str(
        randint(100, 210)) + '"\n"visgroupshown" "1"\n"visgroupautoshown" "1"\n}\n}\n'
    return text

def solid_ceiling(x1, y1, x2, y2, z):
    global solid_count

    solid_count += 1
    id = solid_count
    sid = (id - 2) * 6

    text = 'solid\n{\n"id" "' + str(id) + '"\n'
    text += side(sid + 1, (x2-16, y1+16, z+16), (x1+16, y1+16, z+16), (x1+16, y2-16, z+16), (1, 0, 0, 0), (0, -1, 0, 0))   # top
    text += side(sid + 2, (x2, y2, z), (x1, y2, z), (x1, y1, z), (-1, 0, 0, 0), (0, -1, 0, 0), 'DEV/DEV_MEASUREGENERIC01B')   # bottom
    text += side(sid + 3, (x1+16, y1+16, z+16), (x1, y1, z), (x1, y2, z), (0, -1, 0, 0), (0, 0, -1, 0))   # west (left)
    text += side(sid + 4, (x2-16, y2-16, z+16), (x2, y2, z), (x2, y1, z), (0, 1, 0, 0), (0, 0, -1, 0))   # east (right)
    text += side(sid + 5, (x1+16, y2-16, z+16), (x1, y2, z), (x2, y2, z), (-1, 0, 0, 0), (0, 0, -1, 0))   # north (top)
    text += side(sid + 6, (x2-16, y1+16, z+16), (x2, y1, z), (x1, y1, z), (1, 0, 0, 0), (0, 0, -1, 0))   # south (bottom)
    text += 'editor\n{\n"color" "0 ' + str(randint(100, 210)) + ' ' + str(
        randint(100, 210)) + '"\n"visgroupshown" "1"\n"visgroupautoshown" "1"\n}\n}\n'
    return text

def solid_wall(x, y, z1, z2, l, a):
    global solid_count

    solid_count += 1
    id = solid_count
    sid = (id - 2) * 6

    x2 = x + l*cos(radians(a))
    y2 = y + l*sin(radians(a))

    bv = sqrt(2)*16
    ox = round(bv*cos(radians(a-45)), 6)
    oy = round(bv*sin(radians(a-45)), 6)
    ox2 = round(bv*cos(radians(a-135)), 6)
    oy2 = round(bv*sin(radians(a-135)), 6)

    text = 'solid\n{\n"id" "' + str(id) + '"\n'
    text += side(sid + 1, (x2, y2, z2), (x2+ox2, y2+oy2, z2-16), (x+ox, y+oy, z2-16), (1, 0, 0, 0), (0, -1, 0, 0))
    text += side(sid + 2, (x2+ox2, y2+oy2, z1+16), (x2, y2, z1), (x, y, z1), (-1, 0, 0, 0), (0, -1, 0, 0))
    text += side(sid + 3, (x+ox, y+oy, z2-16), (x+ox, y+oy, z1+16), (x, y, z1), (0, -1, 0, 0), (0, 0, -1, 0))
    text += side(sid + 4, (x2+ox2, y2+oy2, z1+16), (x2+ox2, y2+oy2, z2-16), (x2, y2, z2), (0, 1, 0, 0), (0, 0, -1, 0))
    text += side(sid + 5, (x, y, z2), (x, y, z1), (x2, y2, z1), (-cos(radians(a)), -sin(radians(a)), 0, 0), (0, 0, -1, 0), 'DEV/DEV_MEASUREGENERIC01B')
    text += side(sid + 6, (x+ox, y+oy, z1+16), (x+ox, y+oy, z2-16), (x2+ox2, y2+oy2, z2-16), (cos(radians(a)), sin(radians(a)), 0, 0), (0, 0, -1, 0))
    text += 'editor\n{\n"color" "0 ' + str(randint(100, 210)) + ' ' + str(
        randint(100, 210)) + '"\n"visgroupshown" "1"\n"visgroupautoshown" "1"\n}\n}\n'
    return text


class Room():
    def __init__(self, x, y, z, a=8, b=8, c=8):
        global room_list
        room_list.append(self)

        self.x = x
        self.y = y
        self.z = z
        self.a = a
        self.b = b
        self.c = c

        self.light_count = int(floor((self.a * self.b * self.c) ** (1. / 3) / 5))
        for i in range(self.light_count):
            Light(randint(self.x+1, self.x+self.a-1)*16, randint(self.y+1, self.y+self.b-1)*16, randint(self.z+1, self.z+self.c-1)*16)

    def __str__(self):
        return "room at ("+str(self.x)+","+str(self.y)+","+str(self.z)+") with size ("+str(self.a)+","+str(self.b)+","+str(self.c)+")"

    def walls(self):
        wall_list = []

        wall_list.append(solid_floor(self.x*16, self.y*16, (self.x+self.a)*16, (self.y+self.b)*16, self.z*16))   # floor
        wall_list.append(solid_ceiling(self.x*16, self.y*16, (self.x+self.a)*16, (self.y+self.b)*16, (self.z+self.c)*16))   # ceiling

        wall_list.append(solid_wall(self.x*16, self.y*16, self.z*16, (self.z+self.c)*16, self.a*16, 0))   # south wall (bottom)
        wall_list.append(solid_wall((self.x+self.a)*16, self.y*16, self.z*16, (self.z+self.c)*16, self.b*16, 90))   # east wall (right)
        wall_list.append(solid_wall((self.x+self.a)*16, (self.y+self.b)*16, self.z*16, (self.z+self.c)*16, self.a*16, 180))   # north wall (top)
        wall_list.append(solid_wall(self.x*16, (self.y+self.b)*16, self.z*16, (self.z+self.c)*16, self.b*16, 270))   # west wall (left)

        return wall_list


class Light():
    def __init__(self, x, y, z):
        global instances
        instances.append(self)

        self.x = x
        self.y = y
        self.z = z
        self.id = len(instances)
        self.value = "255 255 255 200"

    def __str__(self):
        s = 'entity\n{\n"id" "'+str(self.id)+'"\n"classname" "light"\n"_light" "'+self.value+'"\n"style" "0"\n'
        s += '"origin" "'+str(self.x)+' '+str(self.y)+' '+str(self.z)+'"\n}\n'
        return s


solid_count = 1
room_list = []
instances = []

r = Room(0, 0, 0, randint(16, 32), randint(16, 32), randint(8, 16))

print("Rooms:")
for room in room_list:
    print(" - " + str(room))

print("Entities:")
for inst in instances:
    print(" - " + str(inst.id))

output("test2.vmf", room_list)