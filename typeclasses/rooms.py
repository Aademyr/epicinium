"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia import DefaultRoom
from evennia.utils import justify


class Room(DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """
    
    
    def return_appearance(self, looker):
        """
        This formats a description. It is the hook a 'look' command
        should call.
        
        Override appearances for room descriptions.

        Args:
            looker (Object): Object doing the looking.
        """
        if not looker:
            return ""
        # get and identify all objects
        visible = (con for con in self.contents if con != looker and
                   con.access(looker, "view"))
        exits, users, things = [], [], []
        for con in visible:
            key = con.get_display_name(looker)
            if con.destination:
                exits.append(key)
            elif con.has_player:
                users.append("%s" % key)
            else:
                things.append(key)
        # get description, build string
        string = "|y%s|n\n" % self.get_display_name(looker)
        desc = self.db.desc
        if desc:
            if not self.tags.get('no-justify'):
                string += '|m' + justify("%s" % desc, align='l') + '\n'
            else:
                string += '|m' + "%s" % desc + '\n'
        if exits:
            string += "|bObvious Exits:\n"
            for ex in exits:
                s = str(ex)
                string += s[:1].upper() + s[1:] + '\n'
        else:
            string += "|bNo Exits!\n"
        if users:
            for u in users:
                string += '|y' + str(u) + ' |gis here.\n'
        if things:
            string += "\n".join(things)
        string += '|n'
        return string
