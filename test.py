import streamlit as st
from PIL import Image
import numpy as np
from keras.models import load_model

# Load the trained model to classify signs
model = load_model('MODEL_INCEPTION.h5')

st.set_page_config(
    page_title="Phan Tấn Vũ",
    page_icon="👋",
    
)
import base64
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("image.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://vapa.vn/wp-content/uploads/2022/12/anh-background-011-1.jpg");
background-size: 200%;
background-position: 30% 45%;
background-repeat: no-repeat;
background-attachment: local;
color:black;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: 50% 45%;
background-size: 400%;
}}
[data-testid="stSidebarNav"] span {{
color:white;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


# Dictionary to label all traffic sign classes
classes = {
    1: 'Hong',
    2: 'MaoDiaHoang',
    3: 'Sen',
    4: 'Su',
    5: 'VanTho',
    6: 'HongMon',
    7: 'ThienDieu',
    8: 'DongTien',
    9: 'HuongDuong',
    10: 'DaUyenThao'
}

# Configure the Streamlit app
st.markdown("<p style='text-align: center ; font-size: 40px; color: blue;'><b>NHẬN DẠNG 10 LOÀI HOA</b></p>", unsafe_allow_html=True)
st.set_option('deprecation.showfileUploaderEncoding', False)

def classify(image):
    image = image.resize((128, 128))
    image = np.expand_dims(image, axis=0)
    image = np.array(image)
    pred = np.argmax(model.predict(image)[0])
    sign = classes[pred + 1]
    return sign

def main():
    st.sidebar.markdown("<p style='text-align: left ; font-size: 27px; color: black;'><b>Nhận Dạng 10 Loài Hoa</b></p>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='text-align: left ; font-size: 18px; color: while;'><b>Phan Tấn Vũ - 20146463</b></p>", unsafe_allow_html=True)
    
    st.sidebar.write("<p style='text-align: left ; font-size: 18px; color: black;'><b>Tải ảnh lên ở đây 👇</b></p>", unsafe_allow_html=True)
    uploaded_file = st.sidebar.file_uploader("", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Ảnh đã tải lên', use_column_width=True)
        sign = classify(image)
        
        if sign == 'Hong':
            st.markdown("<p style='text-align: center; font-size: 30px; color: red;'><b>Hoa Hồng</b></p>", unsafe_allow_html=True)
            st.write("\n")
            st.markdown("**Hồng hay hường là tên gọi chung cho các loài thực vật có hoa dạng cây bụi hoặc cây leo lâu năm thuộc chi Rosa, họ Rosaceae, với hơn 100 loài với màu hoa đa dạng, phân bố từ miền ôn đới đến nhiệt đới. Các loài này nổi tiếng vì hoa đẹp nên thường gọi là hoa hồng. Phần lớn có nguồn gốc bản địa châu Á, số ít còn lại có nguồn gốc bản địa châu Âu, Bắc Mỹ và Tây Bắc Phi. Các loài bản địa, giống cây trồng và cây lai ghép đều được trồng làm cảnh và lấy hương thơm.**")
        if sign == 'MaoDiaHoang':
            st.markdown("<p style='text-align: center; font-size: 30px; color: red;'><b>Hoa Moa Địa Hoàng</b></p>", unsafe_allow_html=True)
            st.write("\n")
            st.markdown("**Mao Địa Hoàng (Scientific name: Solidago virgaurea) là một loài hoa thường được tìm thấy ở các vùng ôn đới. Đặc trưng bởi cụm hoa nhỏ và màu vàng tươi, Mao Địa Hoàng là một loài hoa thực sự quyến rũ. Nó được biết đến với các đặc tính y học và sử dụng trong thuốc truyền thống. Mao Địa Hoàng cũng có ý nghĩa trong việc hỗ trợ sức khỏe tim mạch và hệ miễn dịch. Đây là một loài hoa đáng để khám phá với vẻ đẹp tự nhiên và giá trị y học tiềm năng.**")
        if sign == 'Sen':
            st.markdown("<p style='text-align: center; font-size: 30px; color: red;'><b>Hoa Sen (Quốc hoa của Việt Nam)</b></p>", unsafe_allow_html=True)
            st.write("\n")
            st.markdown("**Sen (Scientific name: Nelumbo nucifera) là loài hoa biểu tượng và được coi là quốc hoa của Việt Nam. Với sắc đẹp tuyệt vời và ý nghĩa sâu sắc, Sen tượng trưng cho sự tinh khiết, tinh tế và sự mạnh mẽ. Loài hoa này thường mọc ở các ao, hồ và đầm lầy, mang đến một cảnh quan thiên nhiên độc đáo. Sen được sử dụng trong nghệ thuật, văn hóa và y học truyền thống, đồng thời còn là biểu tượng của lòng yêu nước và văn hóa Việt Nam.**")
        if sign == 'Su':
            st.markdown("<p style='text-align: center; font-size: 30px; color: red;'><b>Hoa Sứ</b></p>", unsafe_allow_html=True)
            st.write("\n")
            st.markdown("**Sứ (Tên khoa học: Jasminum sambac) là một loài hoa nổi tiếng với mùi hương thơm ngát và vẻ đẹp tinh tế. Được coi là biểu tượng của tình yêu, sự thuần khiết và sự dịu dàng. Sứ thường được trồng trong vườn hoa, sân vườn và sử dụng trong nghi lễ, nghệ thuật và làm mỹ phẩm. Loài hoa này cũng có giá trị y học và được sử dụng trong truyền thống dân gian. Với những đặc điểm độc đáo, Sứ là một loài hoa đáng để khám phá và chiêm ngưỡng.**")
        if sign == 'VanTho':
            st.markdown("<p style='text-align: center; font-size: 30px; color: red;'><b>Hoa Vạn Thọ</b></p>", unsafe_allow_html=True)
            st.write("\n")
            st.markdown("**Vạn Thọ (Tên khoa học: Chrysanthemum morifolium) là một loài hoa phổ biến với nhiều màu sắc và hình dạng đa dạng. Với sự rực rỡ và sự bền vững, Vạn Thọ tượng trưng cho sự giàu có, sự may mắn và sức khỏe. Loài hoa này được trồng trong vườn hoa, sân vườn và thường được sử dụng trong lễ hội và nghi lễ truyền thống. Với vẻ đẹp tuyệt vời và ý nghĩa sâu sắc, Vạn Thọ là một loài hoa đáng để trân trọng và khám phá.**")
        if sign == 'HongMon':
            st.markdown("<p style='text-align: center; font-size: 30px; color: red;'><b>Hoa Hồng Môn</b></p>", unsafe_allow_html=True)
            st.write("\n")
            st.markdown("**Hồng Môn (Tên khoa học: Hibiscus rosa-sinensis) là một loài hoa với những đóa hồng đầy quyến rũ và màu sắc đa dạng. Với vẻ đẹp tuyệt vời và sự thanh lịch, Hồng Môn tượng trưng cho tình yêu, sự mãnh liệt và sự quý phái. Loài hoa này thường được trồng trong vườn hoa, sân vườn và được sử dụng trong trang trí và làm cây cảnh. Hồng Môn còn được sử dụng trong y học truyền thống và có các tác dụng chữa bệnh. Với vẻ đẹp tuyệt vời và ý nghĩa sâu sắc, Hồng Môn là một loài hoa đáng để khám phá và chiêm ngưỡng.**")
        if sign == 'ThienDieu':
            st.markdown("<p style='text-align: center; font-size: 30px; color: red;'><b>Hoa Thiên Điểu</b></p>", unsafe_allow_html=True)
            st.write("\n")
            st.markdown("**Thiên Điểu (Tên khoa học: Dendrobium) là một loài hoa lan nổi tiếng với vẻ đẹp tinh tế và sự kiêu sa. Với hình dạng độc đáo và màu sắc tươi sáng, Thiên Điểu tạo nên một cảnh quan hoa đặc biệt. Loài hoa này thường được trồng trong vườn hoa, nhà kính và được sử dụng trong trang trí nội thất. Thiên Điểu còn được coi là biểu tượng của sự cao quý, sự tinh tế và sự tinh khiết. Với vẻ đẹp độc đáo và ý nghĩa sâu sắc, Thiên Điểu là một loài hoa đáng để khám phá và ngưỡng mộ.**")
        if sign == 'HuongDuong':
            st.markdown("<p style='text-align: center; font-size: 30px; color: red;'><b>Hoa Hướng Dương</b></p>", unsafe_allow_html=True)
            st.write("\n")
            st.markdown("**Hướng Dương (Tên khoa học: Helianthus annuus) là một loài hoa mặt trời với đóa hoa lớn và màu vàng tươi sáng. Với vẻ đẹp rực rỡ và sự tươi vui, Hướng Dương tượng trưng cho niềm hy vọng, sự sáng sủa và năng lượng tích cực. Loài hoa này thường được trồng trong vườn hoa, đồng cỏ và là biểu tượng của mùa hè. Hướng Dương còn được sử dụng trong trang trí, làm thức ăn và dầu hướng dương. Với vẻ đẹp rạng rỡ và ý nghĩa sâu sắc, Hướng Dương là một loài hoa đáng để ngưỡng mộ và yêu thích.**")
        if sign == 'DaUyenThao':
            st.markdown("<p style='text-align: center; font-size: 30px; color: red;'><b>Hoa Dạ Uyên Thảo</b></p>", unsafe_allow_html=True)
            st.write("\n")
            st.markdown("**Dạ Uyên Thảo (Tên khoa học: Orchidaceae) là một loài hoa lan quý hiếm với vẻ đẹp tinh tế và độc đáo. Với hình dạng độc đáo và màu sắc đa dạng, Dạ Uyên Thảo tạo nên một cảnh quan hoa đặc biệt. Loài hoa này thường được trồng trong vườn hoa, nhà kính và được sử dụng trong trang trí nội thất. Dạ Uyên Thảo còn được coi là biểu tượng của sự tinh tế, sự quý phái và sự kiêu sa. Với vẻ đẹp độc đáo và ý nghĩa sâu sắc, Dạ Uyên Thảo là một loài hoa đáng để khám phá và ngưỡng mộ.**")
        if sign == 'DongTien':
            st.markdown("<p style='text-align: center; font-size: 30px; color: red;'><b>Hoa Đồng Tiền</b></p>", unsafe_allow_html=True)
            st.write("\n")
            st.markdown("**Đồng Tiền (Tên khoa học: Lamprocapnos spectabilis) là một loài hoa có nguồn gốc từ vùng núi cao của châu Á. Với những đóa hoa hình trái tim màu hồng hoặc đỏ tươi, Đồng Tiền tạo nên một vẻ đẹp dịu dàng và lãng mạn. Loài hoa này thường được trồng trong vườn hoa, công viên và là biểu tượng của tình yêu và sự lãng mạn. Đồng Tiền còn được sử dụng trong trang trí nội thất và là một loài hoa phổ biến trong các buổi cưới. Với vẻ đẹp đặc trưng và ý nghĩa sâu sắc, Đồng Tiền là một loài hoa đáng để khám phá và trân quý.**")


if __name__ == '__main__':
    main()



