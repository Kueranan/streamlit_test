import streamlit as st 
from PIL import Image  

st.title(" Prediction microplastic * :sunglasses:")

x = st.slider("Fuck you")
st.write(x, "you to", x * x)
##y = st.write("Precission")

coil, coli1, coli2 = st.columns(3)
coil.metric("Precission", "80 %")
coli1.metric("Recall", "70 %")
coli2.metric("mPA", "96 %")


if st.button("about web"):
    st.write("Notthing")
else:
    st.write("About microplastic")
    
image = Image.open('tokito.jpg')
st.image(image, caption= "tokito")

from typing import TYPE_CHECKING, cast

from streamlit.proto.Snow_pb2 import Snow as SnowProto
from streamlit.runtime.metrics_util import gather_metrics

if TYPE_CHECKING:
    from streamlit.delta_generator import DeltaGenerator


class SnowMixin:
    @gather_metrics("snow")
    def snow(self) -> "DeltaGenerator":
        """Draw celebratory snowfall.

        Example
        -------
        >>> import streamlit as st
        >>>
        >>> st.snow()

        ...then watch your app and get ready for a cool celebration!

        """
        snow_proto = SnowProto()
        snow_proto.show = True
        return self.dg._enqueue("snow", snow_proto)

    @property
    def dg(self) -> "DeltaGenerator":
        """Get our DeltaGenerator."""
        return cast("DeltaGenerator", self)

    
    
    


