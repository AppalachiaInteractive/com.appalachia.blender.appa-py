
import bpy
import cspy
from cspy.ui import PT_OPTIONS, PT_, UI
from cspy.polling import POLL
from cspy.nla import *
from cspy.nla_ops import *

def draw_strip_unity_clips(layout, scene):
    strips = get_selected_strips()
    for strip in strips:
        action = strip.action
        if not action:
            continue

        for unity_clip in action.unity_clips:
            if unity_clip.clip_name == strip.name:
                cspy.unity_ui.draw_clip(unity_clip, layout)

def draw_general_nla(layout, scene):
    col = layout.column(align=True, heading='NLA Strips')

    col.operator(NLA_OT_actions_to_strip.bl_idname)

    col.separator(factor=2.0)

    col.prop(scene, 'unity_sheet_dir_path')
    col.operator(NLA_OT_strips_from_text.bl_idname)
    col.operator(NLA_OT_import_strips.bl_idname)

class NLA_EDITOR_PT_UI_Tool_NLA(bpy.types.Panel, PT_, UI.NLA_EDITOR.UI.Tool):
    bl_label = "NLA"
    bl_idname = "NLA_EDITOR_PT_UI_Tool_NLA"
    bl_icon = cspy.icons.NLA

    @classmethod
    def do_poll(cls, context):
        return True
        #return POLL.active_object_animation_data(context)

    def do_draw(self, context, scene, layout, obj):
        box = layout.box()
        box.label(text='NLA')
        draw_general_nla(box, scene)
        box = layout.box()
        box.label(text='Unity Clips')
        draw_strip_unity_clips(box, scene)

        box = layout.box()
        box.operator('pose.transforms_clear')
