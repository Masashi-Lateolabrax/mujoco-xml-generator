import time

import mujoco
import mujoco.viewer

import mujoco_xml_generator as mjc_gen
from mujoco_xml_generator import WorldBody, Body, body


def gen_xml() -> str:
    generator = mjc_gen.Generator().add_children([

        WorldBody().add_children([
            body.Geom(
                type_=body.Geom.GeomType.PLANE, size=(100, 100, 1)
            ),

            Body(
                pos=(0, 0, 100)
            ).add_children([
                body.Joint(type_=body.Joint.JointType.FREE),
                body.Geom(type_=body.Geom.GeomType.SPHERE, size=(1,))
            ])
        ])

    ])
    return generator.build()


def main():
    model = mujoco.MjModel.from_xml_string(xml=gen_xml())
    data = mujoco.MjData(model)

    with mujoco.viewer.launch_passive(model, data) as viewer:
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
