import time

import mujoco
import mujoco.viewer

import mujoco_xml_generator as mjc_gen
import mujoco_xml_generator.common as mjc_cmn
from mujoco_xml_generator import WorldBody, Body, body
from mujoco_xml_generator import Visual, visual


def gen_xml() -> str:
    generator = mjc_gen.Generator().add_children([
        WorldBody().add_children([
            body.Geom(
                type_=mjc_cmn.GeomType.PLANE, pos=(0, 0, 0), size=(10, 10, 1), rgba=(1, 1, 1, 1)
            ),

            Body(
                pos=(0, 0, 10)
            ).add_children([
                body.Joint(type_=body.Joint.JointType.FREE),
                body.Geom(type_=mjc_cmn.GeomType.SPHERE, size=(1,))
            ]),

            Body(
                pos=(0.5, 0.5, 0.6)
            ).add_children([
                body.Joint(type_=body.Joint.JointType.FREE),
                body.Geom(type_=mjc_cmn.GeomType.BOX, size=(0.5, 0.5, 0.5))
            ])
        ])

    ])
    xml = generator.build()
    print(xml)
    return xml


def main():
    model = mujoco.MjModel.from_xml_string(xml=gen_xml())
    data = mujoco.MjData(model)

    with mujoco.viewer.launch_passive(model, data) as viewer:
        viewer.cam.elevation = -10
        viewer.cam.distance = 30

        while viewer.is_running():
            step_start = time.time()

            mujoco.mj_step(model, data)

            with viewer.lock():
                viewer.opt.flags[mujoco.mjtVisFlag.mjVIS_CONTACTPOINT] = int(data.time % 2)

            viewer.sync()

            time_until_next_step = model.opt.timestep - (time.time() - step_start)
            if time_until_next_step > 0:
                time.sleep(time_until_next_step)


if __name__ == '__main__':
    main()
