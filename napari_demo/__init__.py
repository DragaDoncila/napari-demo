from typing import TYPE_CHECKING
import enum
from magicgui import magic_factory
import numpy as np

if TYPE_CHECKING:
    import napari.types


def get_zarr_labels() -> 'napari.types.LabelsData':
    import zarr
    return zarr.zeros((10, 200, 200), chunks=(1, 200, 200), dtype='i1')


# Enums are a convenient way to get a dropdown menu
class Operation(enum.Enum):
    """A set of valid arithmetic operations for image_arithmetic."""

    add = np.add
    subtract = np.subtract
    multiply = np.multiply
    divide = np.divide


def image_arithmetic(
    first_layer: 'napari.types.ImageData',
    operation: Operation,
    second_layer: 'napari.types.ImageData',
) -> 'napari.types.ImageData':
    """Adds, subtracts, multiplies, or divides two same-shaped image layers."""
    return operation.value(first_layer, second_layer)

@magic_factory(
    threshold={"widget_type": "FloatSlider", "max": 25000}
)
def threshold_seg(
        im_layer: 'napari.types.ImageData',
        threshold: int
) -> 'napari.types.LabelsData':
    return im_layer > threshold
