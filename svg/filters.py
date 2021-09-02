from dataclasses import dataclass
from typing import Any, List, Optional, Union
from . import _mixins as m, values, elements as e
from .elements import Element
from typing_extensions import Literal


@dataclass
class Filter(Element, m.FilterPrimitive):
    element_name = "filter"
    elements: Optional[List[Union[
        "FeBlend",
        "FeFlood",
        "FeColorMatrix",
        "FeComponentTransfer",
        "FeComposite",
        "FeConvolveMatrix",
        "FeDiffuseLighting",
        "FeDisplacementMap",
        "FeGaussianBlur",
        "FeImage",
        "FeMerge",
        "FeMorphology",
        "FeOffset",
        "FeSpecularLighting",
        "FeTile",
        "FeTurbulence",
        e.Animate,
        e.Set,
    ]]] = None
    externalResourcesRequired: Optional[Any] = None
    filterUnits: Optional[Any] = None
    primitiveUnits: Optional[Any] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None
    class_: Optional[values.Classes] = None


@dataclass
class FeDistantLight(Element):
    element_name = "feDistantLight"
    azimuth: Optional[Any] = None
    elevation: Optional[Any] = None


@dataclass
class FePointLight(Element, m.FilterPrimitive):
    element_name = "fePointLight"
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    z: Optional[Any] = None


@dataclass
class FeSpotLight(Element, m.FilterPrimitive):
    element_name = "feSpotLight"
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    z: Optional[Any] = None
    pointsAtX: Optional[Any] = None
    pointsAtY: Optional[Any] = None
    pointsAtZ: Optional[Any] = None
    specularExponent: Optional[Any] = None
    limitingConeAngle: Optional[Any] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None


@dataclass
class FeBlend(Element, m.FilterPrimitive):
    element_name = "feBlend"
    in2: Optional[str] = None
    mode: Optional[Any] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None


@dataclass
class FeColorMatrix(Element, m.FilterPrimitive):
    element_name = "feColorMatrix"
    type: Optional[Any] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None
    values: Optional[str] = None


@dataclass
class FeComponentTransfer(Element, m.FilterPrimitive):
    element_name = "feComponentTransfer"
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None


@dataclass
class FeFuncR(Element, m.FilterPrimitive, m.ComponentTransferFunction):
    element_name = "feFuncR"
    type2: Optional[Any] = None


@dataclass
class FeFuncG(Element, m.FilterPrimitive, m.ComponentTransferFunction):
    element_name = "feFuncG"
    type2: Optional[Any] = None


@dataclass
class FeFuncB(Element, m.FilterPrimitive, m.ComponentTransferFunction):
    element_name = "feFuncB"
    type2: Optional[Any] = None


@dataclass
class FeFuncA(Element, m.FilterPrimitive, m.ComponentTransferFunction):
    element_name = "feFuncA"
    type3: Optional[Any] = None


@dataclass
class FeComposite(Element, m.FilterPrimitive):
    element_name = "feComposite"
    in2: Optional[str] = None
    operator: Optional[Any] = None
    k1: Optional[Any] = None
    k2: Optional[Any] = None
    k3: Optional[Any] = None
    k4: Optional[Any] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None


@dataclass
class FeConvolveMatrix(Element, m.FilterPrimitive):
    element_name = "feConvolveMatrix"
    order: Optional[Any] = None
    kernelMatrix: Optional[str] = None
    divisor: Optional[Any] = None
    bias: Optional[Any] = None
    targetX: Optional[Any] = None
    targetY: Optional[Any] = None
    edgeMode: Optional[Literal["duplicate", "wrap", "none"]] = None
    preserveAlpha: Optional[Any] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None


@dataclass
class FeDiffuseLighting(Element, m.FilterPrimitive, m.LightingEffects):
    element_name = "feDiffuseLighting"
    elements: Optional[List[Union[e.Animate, e.Set]]] = None
    surfaceScale: Optional[Any] = None
    diffuseConstant: Optional[Any] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None


@dataclass
class FeDisplacementMap(Element, m.FilterPrimitive):
    element_name = "feDisplacementMap"
    in2: Optional[str] = None
    scale: Optional[Any] = None
    xChannelSelector: Optional[Any] = None
    yChannelSelector: Optional[Any] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None


@dataclass
class FeFlood(Element, m.FilterPrimitive):
    element_name = "feFlood"
    flood_opacity: Optional[values.Opacity] = None
    flood_color: Optional[values.SVGColor] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None


@dataclass
class FeGaussianBlur(Element, m.FilterPrimitive):
    element_name = "feGaussianBlur"
    stdDeviation: Optional[values.NumberOptionalNumber] = None
    edgeMode: Optional[Literal["duplicate", "wrap", "none"]] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None


@dataclass
class FeImage(Element, m.FilterPrimitive):
    element_name = "feImage"
    externalResourcesRequired: Optional[Any] = None
    transform: Optional[Any] = None
    preserveAspectRatio: Optional[values.PreserveAspectRatio] = None
    href: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None


@dataclass
class FeMerge(Element, m.FilterPrimitive):
    element_name = "feMerge"
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None


@dataclass
class FeMergeNode(Element, m.FilterPrimitive):
    element_name = "feMergeNode"
    in_: Optional[str] = None


@dataclass
class FeMorphology(Element, m.FilterPrimitive):
    element_name = "feMorphology"
    operator: Optional[Any] = None
    radius: Optional[Any] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None


@dataclass
class FeOffset(Element, m.FilterPrimitive):
    element_name = "feOffset"
    dx: Optional[Any] = None
    dy: Optional[Any] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None


@dataclass
class FeSpecularLighting(Element, m.FilterPrimitive, m.LightingEffects):
    element_name = "feSpecularLighting"
    elements: Optional[List[Union[e.Animate, e.Set]]] = None
    surfaceScale: Optional[Any] = None
    specularConstant: Optional[Any] = None
    specularExponent: Optional[Any] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None


@dataclass
class FeTile(Element, m.FilterPrimitive):
    element_name = "feTile"
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None


@dataclass
class FeTurbulence(Element, m.FilterPrimitive):
    element_name = "feTurbulence"
    baseFrequency: Optional[str] = None
    numOctaves: Optional[Any] = None
    seed: Optional[Any] = None
    stitchTiles: Optional[Any] = None
    type: Optional[Any] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None
