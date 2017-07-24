'''
This module contains functionality for managing the wildlands outdoor
area. Items handled include the display of the local map to the player,
effects such as fire, smoke, moving fluids, heightmap based rendering
effects, as well as dynamic allocation, compression and full deallocation
of rooms as needed resulting from player or NPC interaction.
'''
from django.conf import settings
from world.wild_settings import *

from typeclasses.metaclasses import Singleton
from typeclasses.rooms import WildRoom

from evennia.utils import create

EXIT_TYPECLASS = settings.BASE_EXIT_TYPECLASS

from PIL import Image

class WildRoomManager(object):
    '''
    Singleton manager object for dealing with dynamic allocating and
    deallocating of wild map rooms in response to interaction with
    players / objects / environment / NPCs etc.
    '''
    
    __metaclass__ = Singleton
    
    '''
    State of any allocated wilderness rooms indexed by map coordinates.
    Possible values:
    'active'  : Fully allocated and active, functions like a normal room.
    'dormant' : Still in memory but all data is compressed. This can be
                because it hasn't yet timed out or it may contain an
                object with the tag no-dealloc which prevents full deallocation.
    '''
    roomStates = {
    }
    
    '''
    All other wild map rooms are completely deallocated from memory.
    Maps are generated from the base ascii sequence without waking them.
    '''
    
    def __init__(self):
        '''
        Read the map file images into memory for use in the outdoor rooms.
        '''
        self.loadMapBitmaps()
    
    def awake(self, coords):
        '''
        Test if a wilderness room is allocated or not.
        '''
        try:
            if self.roomStates[coords] is 'active':
                return True
            else:
                return False
        except KeyError:
            return False
    
    def loadMapBitmaps(self, biomeRGBhA_file = BIOME_HEIGHT_IMAGE_FILE):
        '''
        Load the RGB array from the map image into memory
        TODO:
        - Profile and optimize
        - Add other map data - height moisture etc.
        - Deallocate this gracefully on shutdown
        
        Right now the map is small and having it all in memory isn't a big
        deal. However with more data layers it may become necessary to implement
        some kind of paging optimization.
        '''
        self.biomeRGBhA_image = Image.open(biomeRGBhA_file)
        self.biomeRGBhA = self.biomeRGBhA_image.load()
        
        # RGBA values are now available via self.biomeRGBhA[x,y]
    
    def loadMapPage(self, coords):
        '''
        Loads a page of map data into memory. Note this does NOT activate
        the rooms themselves, it only makes the map data accessible.
        Required by various map displaying / tile probing functions.
        '''
        pass
    
    def getDefaultInfo(self, coords):
        '''
        A fast index of default room information for dormant map tiles.
        Useful for looking up data for biome data about unallocated wild rooms.
        '''
        pass
    
    def getRoomInfo(self, coords):
        '''
        Return a dict of all possible attributes we can ascertain about
        the desired coordinate without changing its allocation state.
        Useful for things like naming rooms without having to allocate them,
        getting heights for rendering, etc.
        
        We will do this differently depending on the state of the room
        '''
        data = {}
        
        try:
            if self.roomStates[coords] is 'dormant':
                # Room contains extra information, decompress it temporarily
                self.wakeup(coords, self)
        except KeyError:
            # Deallocated room - use precomputed version
            # If out of bounds an exception will be raised.
            return self.getDefaultInfo(coords)
    
    def wakeup(self, coords, caller = None, sourceExit = None, exitCommandString = None):
        '''
        Used to bring a wild room to full functional capacity as a normal
        room. If it was not previously allocated we spawn a new room object.
        If it was in a dormant compressed state, unzip its state and reinstate
        it as a normal room.
        
        Args:
            coords      :   X Y coordinates of the wild room.
            caller      :   Traversing object that is waking this room up, if any.
            sourceExit  :   Exit that woke this map room
            exitCommandString   :   Exit command that woke this room, if any.
                                    Used to determine opposites of cardinal dirs.
        
        TODO: Add compressed dormant state handling
        '''
        
        roomInfo = self.getRoomInfo(coords)

        #location = caller.location

        # create new room
        new_room = create.create_object(WildRoom,
                                        roomInfo['name'],
                                        aliases=roomInfo["aliases"],
                                        report_to=caller)
        lockstring =    "control:perm(Wizards); " \
                        "delete:perm(Wizards); " \
                        "edit:perm(Wizards)"
        new_room.locks.add(lockstring)
        '''
        if new_room.aliases.all():
            alias_string = " (%s)" % ", ".join(new_room.aliases.all())
        room_string = "Created room %s(%s)%s of type %s." % (new_room,
                                        new_room.dbref, alias_string, typeclass)
        '''

        # create exit to room

        exit_to_string = ""
        exit_back_string = ""
        
        # Make an exit back to the source that woke this room
        if not sourceRoom:
            raise NameError('WildRoomManager().wakeup(): Attempted to wake a wild room %s from a non-existant source room.', str(coords))
        
        '''
        if self.rhs_objs:
            to_exit = self.rhs_objs[0]
            if not to_exit["name"]:
                exit_to_string = \
                    "\nNo exit created to new room."
            elif not location:
                exit_to_string = \
                  "\nYou cannot create an exit from a None-location."
        '''
        '''
        Determine an appropriate opposing alias.
        Unless this lookup fails wild rooms will typically only have
        one alias per direction.
        TODO: Volumetric voxel terrain map ???
        '''
        dirOpposites = {
            'n' : 's',
            'e' : 'w',
            'w' : 'e',
            's' : 'n',
            'u' : 'd',
            'd' : 'u',
            'north' : 'south',
            'east'  : 'west',
            'west'  : 'east',
            'south' : 'north',
            'up'    : 'down',
            'down'  : 'up',
        }
        try:
            exitAlias = dirOpposites[exitCommandString]
        except KeyError:
            # The exit command used had some other name so just copy that.
            # E.g. 'bridge' or 'river'. This will only happen connecting
            # to non-map rooms so shouldn't interrupt the flow of map movement.
            exitAlias = exitCommandString
        
        new_exit = create.create_object(EXIT_TYPECLASS,
                                        new_room,
                                        aliases=[exitAlias],
                                        locks=lockstring,
                                        destination=sourceRoom,
                                        report_to=caller,
                                        )
        
        
'''        
            else:
                # Build the exit to the new room from the current one
                typeclass = to_exit["option"]
                if not typeclass:
                    typeclass = settings.BASE_EXIT_TYPECLASS

                new_to_exit = create.create_object(typeclass, to_exit["name"],
                                                   location,
                                                   aliases=to_exit["aliases"],
                                                   locks=lockstring,
                                                   destination=new_room,
                                                   report_to=caller)
                alias_string = ""
                if new_to_exit.aliases.all():
                    alias_string = " (%s)" % ", ".join(new_to_exit.aliases.all())
                exit_to_string = "\nCreated Exit from %s to %s: %s(%s)%s."
                exit_to_string = exit_to_string % (location.name,
                                                   new_room.name,
                                                   new_to_exit,
                                                   new_to_exit.dbref,
                                                   alias_string)

        # Create exit back from new room

        if len(self.rhs_objs) > 1:
            # Building the exit back to the current room
            back_exit = self.rhs_objs[1]
            if not back_exit["name"]:
                exit_back_string = \
                    "\nNo back exit created."
            elif not location:
                exit_back_string = \
                   "\nYou cannot create an exit back to a None-location."
            else:
                typeclass = back_exit["option"]
                if not typeclass:
                    typeclass = settings.BASE_EXIT_TYPECLASS
                new_back_exit = create.create_object(typeclass,
                                                   back_exit["name"],
                                                   new_room,
                                                   aliases=back_exit["aliases"],
                                                   locks=lockstring,
                                                   destination=location,
                                                   report_to=caller)
                alias_string = ""
                if new_back_exit.aliases.all():
                    alias_string = " (%s)" % ", ".join(new_back_exit.aliases.all())
                exit_back_string = "\nCreated Exit back from %s to %s: %s(%s)%s."
                exit_back_string = exit_back_string % (new_room.name,
                                                       location.name,
                                                       new_back_exit,
                                                       new_back_exit.dbref,
                                                       alias_string)
        caller.msg("%s%s%s" % (room_string, exit_to_string, exit_back_string))
        if new_room and ('teleport' in self.switches or "tel" in self.switches):
            caller.move_to(new_room)
'''
