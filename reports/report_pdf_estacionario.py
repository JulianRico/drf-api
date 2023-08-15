def GeneratePDFintoSVG(questions_mtto, question_views, questions_deterioration, tank_identification,
                       observations_and_results, signatures, photos, fecha_convertida):

    print(questions_mtto)
    print(question_views)
    print(questions_deterioration)
    print(tank_identification)
    print(observations_and_results)
    print(signatures)
    print(photos)
    print(fecha_convertida)

    svg_code = f"""
    <svg
   width="8.5in"
   height="14in"
   viewBox="0 0 215.9 355.6"
   version="1.1"
   id="svg5"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:dc="http://purl.org/dc/elements/1.1/">
  <defs
     id="defs2">
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath1">
      <path
         d="M 0,0 H 1656.7181 V 2862.3496 H 0 Z"
         id="path10272" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath2">
      <path
         d="M 1.1716535,1.1716535 H 1656.7181 V 2862.3496 H 1.1716535 Z"
         id="path10275" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath3">
      <path
         d="m 421.79528,1448.1638 h 65.61259 v 42.1795 h -65.61259 z"
         id="path10278" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath4">
      <path
         d="m 421.79528,1702.4126 h 65.61259 v 42.1795 h -65.61259 z"
         id="path10281" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath6">
      <path
         d="M 1.1716535,2135.9244 H 353.83937 v 42.1795 H 1.1716535 Z"
         id="path10287" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath9">
      <path
         d="M 1.1716535,2549.5181 H 274.16693 v 24.6047 H 1.1716535 Z"
         id="path10296" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath10">
      <path
         d="M 1.1716535,2575.2945 H 274.16693 v 24.6047 H 1.1716535 Z"
         id="path10299" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath11">
      <path
         d="M 1.1716535,2601.0709 H 274.16693 v 24.6047 H 1.1716535 Z"
         id="path10302" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath12">
      <path
         d="M 1.1716535,2360.8819 H 224.95748 v 24.6047 H 1.1716535 Z"
         id="path10305" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath13">
      <path
         d="M 1.1716535,2626.8472 H 274.16693 v 24.6048 H 1.1716535 Z"
         id="path10308" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath14">
      <path
         d="M 1.1716535,2386.6583 H 420.62362 v 37.4929 H 1.1716535 Z"
         id="path10311" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath15">
      <path
         d="M 1.1716535,2652.6236 H 1655.5465 V 2861.178 H 1.1716535 Z"
         id="path10314" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath16">
      <path
         d="M 1.1716535,2497.9654 H 274.16693 v 24.6047 H 1.1716535 Z"
         id="path10317" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath19">
      <path
         d="M 1.1716535,2523.7417 H 274.16693 v 24.6048 H 1.1716535 Z"
         id="path10326" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath20">
      <path
         d="M 1.1716535,2005.8709 H 353.83937 v 42.1795 H 1.1716535 Z"
         id="path10329" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath22">
      <path
         d="M 1.1716535,2049.222 H 353.83937 v 42.1796 H 1.1716535 Z"
         id="path10335" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath24">
      <path
         d="M 1.1716535,2092.5732 H 353.83937 v 42.1796 H 1.1716535 Z"
         id="path10341" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath26">
      <path
         d="M 1.1716535,2425.3228 H 1655.5465 v 37.4929 H 1.1716535 Z"
         id="path10347" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath27">
      <path
         d="M 1.1716535,2463.9874 H 274.16693 v 32.8063 H 1.1716535 Z"
         id="path10350" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath28">
      <path
         d="m 275.33858,2463.9874 h 422.96693 v 32.8063 H 275.33858 Z"
         id="path10353" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath29">
      <path
         d="m 699.47717,2463.9874 h 956.06933 v 32.8063 H 699.47717 Z"
         id="path10356" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath30">
      <path
         d="M 1.1716535,2179.2756 H 1655.5465 v 39.8362 H 1.1716535 Z"
         id="path10359" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath31">
      <path
         d="M 1.1716535,2220.2835 H 1655.5465 v 22.2614 H 1.1716535 Z"
         id="path10362" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath33">
      <path
         d="M 1.1716535,2337.4488 H 1655.5465 v 22.2614 H 1.1716535 Z"
         id="path10368" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath34">
      <path
         d="m 226.12913,2360.8819 h 127.71024 v 24.6047 H 226.12913 Z"
         id="path10371" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath35">
      <path
         d="m 421.79528,2360.8819 h 276.51023 v 24.6047 H 421.79528 Z"
         id="path10374" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath36">
      <path
         d="m 843.59055,2360.8819 h 287.05515 v 24.6047 H 843.59055 Z"
         id="path10377" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath38">
      <path
         d="M 1.1716535,1832.4661 H 353.83937 v 42.1796 H 1.1716535 Z"
         id="path10383" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath40">
      <path
         d="M 1.1716535,1962.5197 H 353.83937 v 42.1795 H 1.1716535 Z"
         id="path10389" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath42">
      <path
         d="M 1.1716535,1919.1685 H 353.83937 v 42.1795 H 1.1716535 Z"
         id="path10395" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath44">
      <path
         d="M 1.1716535,1875.8173 H 353.83937 v 42.1796 H 1.1716535 Z"
         id="path10401" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath46">
      <path
         d="M 1.1716535,1702.4126 H 353.83937 v 42.1795 H 1.1716535 Z"
         id="path10407" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath48">
      <path
         d="M 1.1716535,1745.7638 H 353.83937 v 42.1795 H 1.1716535 Z"
         id="path10413" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath50">
      <path
         d="M 1.1716535,1789.115 H 353.83937 v 42.1795 H 1.1716535 Z"
         id="path10419" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath53">
      <path
         d="M 1.1716535,1596.9638 H 133.5685 v 104.2771 H 1.1716535 Z"
         id="path10428" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath54">
      <path
         d="m 134.74016,1596.9638 h 219.09921 v 33.9779 H 134.74016 Z"
         id="path10431" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath56">
      <path
         d="m 134.74016,1632.1134 h 219.09921 v 33.9779 H 134.74016 Z"
         id="path10437" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath58">
      <path
         d="m 134.74016,1667.263 h 219.09921 v 33.9779 H 134.74016 Z"
         id="path10443" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath60">
      <path
         d="m 134.74016,1404.8126 h 219.09921 v 42.1795 H 134.74016 Z"
         id="path10449" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath62">
      <path
         d="M 1.1716535,1448.1638 H 353.83937 v 42.1795 H 1.1716535 Z"
         id="path10455" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath63">
      <path
         d="M 555.36378,1448.1638 H 1655.5465 v 42.1795 H 555.36378 Z"
         id="path10458" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath64">
      <path
         d="M 1.1716535,1491.515 H 133.5685 v 104.2771 H 1.1716535 Z"
         id="path10461" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath65">
      <path
         d="m 134.74016,1491.515 h 219.09921 v 33.9779 H 134.74016 Z"
         id="path10464" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath67">
      <path
         d="m 134.74016,1526.6646 h 219.09921 v 33.9779 H 134.74016 Z"
         id="path10470" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath69">
      <path
         d="m 134.74016,1561.8142 h 219.09921 v 33.9779 H 134.74016 Z"
         id="path10476" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath70">
      <path
         d="M 1.1716535,1231.4079 H 133.5685 v 42.1795 H 1.1716535 Z"
         id="path10479" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath71">
      <path
         d="m 134.74016,1231.4079 h 219.09921 v 42.1795 H 134.74016 Z"
         id="path10482" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath72">
      <path
         d="m 555.36378,1231.4079 h 863.50862 v 42.1795 H 555.36378 Z"
         id="path10485" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath73">
      <path
         d="M 1.1716535,1274.7591 H 133.5685 v 172.233 H 1.1716535 Z"
         id="path10488" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath74">
      <path
         d="m 134.74016,1274.7591 h 219.09921 v 42.1795 H 134.74016 Z"
         id="path10491" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath76">
      <path
         d="m 134.74016,1318.1102 h 219.09921 v 42.1796 H 134.74016 Z"
         id="path10497" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath78">
      <path
         d="m 134.74016,1361.4614 h 219.09921 v 42.1795 H 134.74016 Z"
         id="path10503" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath80">
      <path
         d="M 1.1716535,1033.3984 H 353.83937 v 42.1796 H 1.1716535 Z"
         id="path10509" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath81">
      <path
         d="m 555.36378,1033.3984 h 863.50862 v 42.1796 H 555.36378 Z"
         id="path10512" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath82">
      <path
         d="M 1.1716535,1076.7496 H 133.5685 v 153.4866 H 1.1716535 Z"
         id="path10515" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath83">
      <path
         d="m 134.74016,1076.7496 h 219.09921 v 42.1795 H 134.74016 Z"
         id="path10518" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath84">
      <path
         d="m 555.36378,1076.7496 h 863.50862 v 42.1795 H 555.36378 Z"
         id="path10521" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath85">
      <path
         d="m 134.74016,1120.1008 h 219.09921 v 66.7842 H 134.74016 Z"
         id="path10524" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath86">
      <path
         d="m 555.36378,1120.1008 h 863.50862 v 66.7842 H 555.36378 Z"
         id="path10527" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath87">
      <path
         d="m 134.74016,1188.0567 h 219.09921 v 42.1795 H 134.74016 Z"
         id="path10530" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath88">
      <path
         d="m 555.36378,1188.0567 h 863.50862 v 42.1795 H 555.36378 Z"
         id="path10533" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath89">
      <path
         d="m 134.74016,859.9937 h 219.09921 v 42.17953 H 134.74016 Z"
         id="path10536" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath91">
      <path
         d="M 1.1716535,903.34488 H 353.83937 V 1032.2268 H 1.1716535 Z"
         id="path10542" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath92">
      <path
         d="m 555.36378,903.34488 h 863.50862 v 42.17953 H 555.36378 Z"
         id="path10545" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath93">
      <path
         d="m 555.36378,946.69606 h 863.50862 v 42.17953 H 555.36378 Z"
         id="path10548" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath94">
      <path
         d="m 555.36378,990.04724 h 863.50862 v 42.17956 H 555.36378 Z"
         id="path10551" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath95">
      <path
         d="M 1.1716535,686.58898 H 133.5685 V 728.7685 H 1.1716535 Z"
         id="path10554" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath96">
      <path
         d="M 134.74016,686.58898 H 353.83937 V 728.7685 H 134.74016 Z"
         id="path10557" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath97">
      <path
         d="M 555.36378,686.58898 H 1418.8724 V 728.7685 H 555.36378 Z"
         id="path10560" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath98">
      <path
         d="M 1.1716535,729.94016 H 133.5685 V 902.17323 H 1.1716535 Z"
         id="path10563" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath99">
      <path
         d="m 134.74016,729.94016 h 219.09921 v 42.17953 H 134.74016 Z"
         id="path10566" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath101">
      <path
         d="m 134.74016,773.29134 h 219.09921 v 42.17953 H 134.74016 Z"
         id="path10572" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath103">
      <path
         d="m 134.74016,816.64252 h 219.09921 v 42.17953 H 134.74016 Z"
         id="path10578" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath104">
      <path
         d="m 555.36378,816.64252 h 863.50862 v 42.17953 H 555.36378 Z"
         id="path10581" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath105">
      <path
         d="M 1.1716535,619.80472 H 224.95748 V 645.5811 H 1.1716535 Z"
         id="path10584" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath106">
      <path
         d="M 226.12913,619.80472 H 1655.5465 V 645.5811 H 226.12913 Z"
         id="path10587" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath107">
      <path
         d="M 1.1716535,646.75276 H 353.83937 v 38.66456 H 1.1716535 Z"
         id="path10590" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath108">
      <path
         d="m 355.01102,646.75276 h 199.18111 v 18.74645 H 355.01102 Z"
         id="path10593" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath109">
      <path
         d="m 555.36378,646.75276 h 863.50862 v 38.66456 H 555.36378 Z"
         id="path10596" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath110">
      <path
         d="m 1420.0441,646.75276 h 117.1653 v 38.66456 h -117.1653 z"
         id="path10599" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath111">
      <path
         d="m 1538.3811,646.75276 h 117.1654 v 38.66456 h -117.1654 z"
         id="path10602" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath114">
      <path
         d="m 843.59055,351.49606 h 811.95595 v 43.35118 H 843.59055 Z"
         id="path10611" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath115">
      <path
         d="M 1.1716535,440.54173 H 133.5685 v 43.35118 H 1.1716535 Z"
         id="path10614" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath116">
      <path
         d="M 1.1716535,485.06457 H 133.5685 v 43.35118 H 1.1716535 Z"
         id="path10617" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath117">
      <path
         d="M 1.1716535,592.85669 H 133.5685 v 25.77638 H 1.1716535 Z"
         id="path10620" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath118">
      <path
         d="m 275.33858,592.85669 h 145.28504 v 25.77638 H 275.33858 Z"
         id="path10623" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath119">
      <path
         d="m 488.57953,592.85669 h 209.72598 v 25.77638 H 488.57953 Z"
         id="path10626" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath120">
      <path
         d="m 843.59055,592.85669 h 287.05515 v 25.77638 H 843.59055 Z"
         id="path10629" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath123">
      <path
         d="M 488.57953,1.1716535 H 1274.7591 V 30.462992 H 488.57953 Z"
         id="path10638" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath124">
      <path
         d="M 488.57953,31.634646 H 1274.7591 V 50.381102 H 488.57953 Z"
         id="path10641" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath125">
      <path
         d="M 488.57953,51.552756 H 1274.7591 V 73.814173 H 488.57953 Z"
         id="path10644" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath126">
      <path
         d="M 488.57953,74.985827 H 1274.7591 V 97.247244 H 488.57953 Z"
         id="path10647" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath127">
      <path
         d="m 1275.9307,1.1716535 h 379.6158 V 30.462992 h -379.6158 z"
         id="path10650" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath128">
      <path
         d="m 1275.9307,31.634646 h 379.6158 v 18.746456 h -379.6158 z"
         id="path10653" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath129">
      <path
         d="m 1275.9307,51.552756 h 379.6158 v 22.261417 h -379.6158 z"
         id="path10656" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath130">
      <path
         d="m 1275.9307,74.985827 h 379.6158 v 45.694483 h -379.6158 z"
         id="path10659" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath131">
      <path
         d="M 488.57953,98.418898 H 1274.7591 V 120.68031 H 488.57953 Z"
         id="path10662" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath132">
      <path
         d="M 1.1716535,529.5874 H 1655.5465 v 30.46299 H 1.1716535 Z"
         id="path10665" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath133">
      <path
         d="M 1.1716535,561.22205 H 133.5685 v 30.46299 H 1.1716535 Z"
         id="path10668" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath134">
      <path
         d="m 421.79528,561.22205 h 276.51023 v 30.46299 H 421.79528 Z"
         id="path10671" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath136">
      <path
         d="m 1420.0441,396.0189 h 235.5024 v 43.35118 h -235.5024 z"
         id="path10677" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath137">
      <path
         d="m 843.59055,396.0189 h 287.05515 v 43.35118 H 843.59055 Z"
         id="path10680" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath138">
      <path
         d="m 843.59055,485.06457 h 287.05515 v 43.35118 H 843.59055 Z"
         id="path10683" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath139">
      <path
         d="M 1.1716535,306.97323 H 133.5685 v 43.35118 H 1.1716535 Z"
         id="path10686" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath140">
      <path
         d="M 1.1716535,351.49606 H 133.5685 v 43.35118 H 1.1716535 Z"
         id="path10689" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath141">
      <path
         d="M 1.1716535,396.0189 H 133.5685 v 43.35118 H 1.1716535 Z"
         id="path10692" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath143">
      <path
         d="m 843.59055,440.54173 h 287.05515 v 43.35118 H 843.59055 Z"
         id="path10698" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath145">
      <path
         d="M 1.1716535,212.06929 H 554.19213 V 249.5622 H 1.1716535 Z"
         id="path10704" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath146">
      <path
         d="M 1.1716535,145.28504 H 1655.5465 v 28.11968 H 1.1716535 Z"
         id="path10707" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath147">
      <path
         d="M 1.1716535,174.57638 H 1655.5465 v 36.32126 H 1.1716535 Z"
         id="path10710" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath148">
      <path
         d="M 555.36378,212.06929 H 1655.5465 V 249.5622 H 555.36378 Z"
         id="path10713" />
    </clipPath>
    <clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath149">
      <path
         d="M 1.1716535,250.73386 H 133.5685 v 55.06771 H 1.1716535 Z"
         id="path10716" />
    </clipPath>
  </defs>
  <g
     id="layer1"
     style="display:inline">
    <path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 224.95748,560.05039 h 50.3811 v 32.8063 h -50.3811 z"
       id="path10739"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 353.83937,560.05039 h 67.95591 v 32.8063 h -67.95591 z"
       id="path10741"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.279423"
       y="72.520256"
       id="text30644-9"><tspan
         id="tspan30642-9"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.279423"
         y="72.520256">X</tspan></text>
    <path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 842.4189,560.05039 h 145.28504 v 32.8063 H 842.4189 Z"
       id="path10743"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="118.51374"
       y="72.430695"
       id="text30644-5"><tspan
         id="tspan30642-90"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="118.51374"
         y="72.430695">X</tspan></text>
    <path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 1130.6457,560.05039 h 145.285 v 32.8063 h -145.285 z"
       id="path10745"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="156.31049"
       y="72.341133"
       id="text30644-2"><tspan
         id="tspan30642-79"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="156.31049"
         y="72.341133">X</tspan></text>
    <path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 224.95748,591.68504 h 50.3811 v 28.11968 h -50.3811 z"
       id="path10747"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="31.464067"
       y="76.304413"
       id="text30644-1"><tspan
         id="tspan30642-0"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="31.464067"
         y="76.304413">X</tspan></text>
    <path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 420.62362,591.68504 h 67.95591 v 28.11968 h -67.95591 z"
       id="path10749"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.415131"
       y="76.37159"
       id="text30644-7"><tspan
         id="tspan30642-3"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.415131"
         y="76.37159">X</tspan></text>
    <path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 698.30551,591.68504 h 145.28504 v 28.11968 H 698.30551 Z"
       id="path10751"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="99.615372"
       y="76.282021"
       id="text30644-8"><tspan
         id="tspan30642-7"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="99.615372"
         y="76.282021">X</tspan></text>
    <path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 1130.6457,591.68504 h 145.285 v 28.11968 h -145.285 z"
       id="path10753"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="156.57918"
       y="76.461151"
       id="text30644-57"><tspan
         id="tspan30642-8"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="156.57918"
         y="76.461151">X</tspan></text>
    <path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 1418.8724,591.68504 h 119.5087 v 28.11968 h -119.5087 z"
       id="path10755"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="191.95766"
       y="76.37159"
       id="text30644-19"><tspan
         id="tspan30642-4"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.95766"
         y="76.37159">X</tspan></text>
    <path
       style="fill:#eefc98;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 0,2336.2772 h 1656.7181 v 24.6047 H 0 Z"
       id="path10757"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 353.83937,2359.7102 h 67.95591 v 26.9481 h -67.95591 z"
       id="path10759"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 1130.6457,2359.7102 h 145.285 v 26.9481 h -145.285 z"
       id="path10761"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 420.62362,2385.4866 h 67.95591 v 39.8362 h -67.95591 z"
       id="path10763"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 0,2462.8157 h 1656.7181 v 35.1497 H 0 Z"
       id="path10765"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.68895"
       y="167.45995"
       id="text30644-85-89-235-6"><tspan
         id="tspan30642-905-67-42-8"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.68895"
         y="167.45995">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.77852"
       y="162.17557"
       id="text30644-85-89-235-64"><tspan
         id="tspan30642-905-67-42-0"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.77852"
         y="162.17557">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.68895"
       y="156.6225"
       id="text30644-85-89-235-0"><tspan
         id="tspan30642-905-67-42-1"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.68895"
         y="156.6225">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.68895"
       y="178.20784"
       id="text30644-85-89-235-4"><tspan
         id="tspan30642-905-67-42-9"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.68895"
         y="178.20784">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.77852"
       y="172.92346"
       id="text30644-85-89-235-9"><tspan
         id="tspan30642-905-67-42-2"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.77852"
         y="172.92346">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="66.565613"
       y="178.29739"
       id="text30644-55"><tspan
         id="tspan30642-54"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="66.565613"
         y="178.29739">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="57.9673"
       y="178.29739"
       id="text30644-34"><tspan
         id="tspan30642-21"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="57.9673"
         y="178.29739">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.279423"
       y="178.20784"
       id="text30644-60"><tspan
         id="tspan30642-605"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.279423"
         y="178.20784">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="66.655174"
       y="172.83389"
       id="text30644-74"><tspan
         id="tspan30642-08"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="66.655174"
         y="172.83389">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.415127"
       y="172.92346"
       id="text30644-71"><tspan
         id="tspan30642-47"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.415127"
         y="172.92346">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.548119"
       y="172.83389"
       id="text30644-97"><tspan
         id="tspan30642-64"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.548119"
         y="172.83389">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="66.565613"
       y="167.45995"
       id="text30644-05"><tspan
         id="tspan30642-26"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="66.565613"
         y="167.45995">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.504692"
       y="167.54951"
       id="text30644-119"><tspan
         id="tspan30642-500"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.504692"
         y="167.54951">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.637684"
       y="167.37038"
       id="text30644-68"><tspan
         id="tspan30642-94"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.637684"
         y="167.37038">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="66.565613"
       y="162.26514"
       id="text30644-907"><tspan
         id="tspan30642-63"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="66.565613"
         y="162.26514">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.146431"
       y="162.26514"
       id="text30644-83"><tspan
         id="tspan30642-02"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.146431"
         y="162.26514">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.189857"
       y="162.086"
       id="text30644-260"><tspan
         id="tspan30642-60"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.189857"
         y="162.086">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.192574"
       y="156.80162"
       id="text30644-38"><tspan
         id="tspan30642-781"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.192574"
         y="156.80162">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.594261"
       y="156.80162"
       id="text30644-67"><tspan
         id="tspan30642-24"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.594261"
         y="156.80162">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.458553"
       y="156.6225"
       id="text30644-64"><tspan
         id="tspan30642-685"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.458553"
         y="156.6225">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.282135"
       y="151.06941"
       id="text30644-317"><tspan
         id="tspan30642-715"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.282135"
         y="151.06941">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.235996"
       y="151.69638"
       id="text30644-79"><tspan
         id="tspan30642-83"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.235996"
         y="151.69638">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.368988"
       y="151.42767"
       id="text30644-359"><tspan
         id="tspan30642-226"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.368988"
         y="151.42767">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.504692"
       y="144.71025"
       id="text30644-84"><tspan
         id="tspan30642-66"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.504692"
         y="144.71025">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.279423"
       y="144.79982"
       id="text30644-410"><tspan
         id="tspan30642-58"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.279423"
         y="144.79982">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.371704"
       y="137.54498"
       id="text30644-18"><tspan
         id="tspan30642-62"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.371704"
         y="137.54498">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.773392"
       y="137.63455"
       id="text30644-316"><tspan
         id="tspan30642-29"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.773392"
         y="137.63455">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.100292"
       y="137.27629"
       id="text30644-69"><tspan
         id="tspan30642-50"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.100292"
         y="137.27629">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.103004"
       y="132.17105"
       id="text30644-80"><tspan
         id="tspan30642-36"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.103004"
         y="132.17105">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.146431"
       y="132.17105"
       id="text30644-94"><tspan
         id="tspan30642-51"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.146431"
         y="132.17105">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.279423"
       y="132.08148"
       id="text30644-54"><tspan
         id="tspan30642-27"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.279423"
         y="132.08148">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.192574"
       y="126.7971"
       id="text30644-11"><tspan
         id="tspan30642-03"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.192574"
         y="126.7971">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.683826"
       y="126.7971"
       id="text30644-32"><tspan
         id="tspan30642-688"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.683826"
         y="126.7971">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.548119"
       y="126.61797"
       id="text30644-41"><tspan
         id="tspan30642-68"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.548119"
         y="126.61797">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.282135"
       y="121.42316"
       id="text30644-13"><tspan
         id="tspan30642-20"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.282135"
         y="121.42316">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.594261"
       y="121.33359"
       id="text30644-31"><tspan
         id="tspan30642-17"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.594261"
         y="121.33359">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.189857"
       y="121.33359"
       id="text30644-53"><tspan
         id="tspan30642-799"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.189857"
         y="121.33359">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.192574"
       y="116.04921"
       id="text30644-231"><tspan
         id="tspan30642-000"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.192574"
         y="116.04921">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.415127"
       y="116.31791"
       id="text30644-237"><tspan
         id="tspan30642-57"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.415127"
         y="116.31791">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.727253"
       y="115.95965"
       id="text30644-20"><tspan
         id="tspan30642-84"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.727253"
         y="115.95965">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.103004"
       y="110.67527"
       id="text30644-90"><tspan
         id="tspan30642-6"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.103004"
         y="110.67527">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.773392"
       y="110.5857"
       id="text30644-26"><tspan
         id="tspan30642-93"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.773392"
         y="110.5857">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.727253"
       y="110.49613"
       id="text30644-52"><tspan
         id="tspan30642-22"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.727253"
         y="110.49613">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.013443"
       y="105.12219"
       id="text30644-873"><tspan
         id="tspan30642-2"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.013443"
         y="105.12219">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.056866"
       y="105.39089"
       id="text30644-72"><tspan
         id="tspan30642-5"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.056866"
         y="105.39089">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.637684"
       y="105.03262"
       id="text30644-23"><tspan
         id="tspan30642-00"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.637684"
         y="105.03262">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.013443"
       y="99.569115"
       id="text30644-87"><tspan
         id="tspan30642-49"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.013443"
         y="99.569115">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.773392"
       y="99.837814"
       id="text30644-77"><tspan
         id="tspan30642-42"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.773392"
         y="99.837814">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.279423"
       y="99.837814"
       id="text30644-0"><tspan
         id="tspan30642-11"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.279423"
         y="99.837814">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.192574"
       y="94.642998"
       id="text30644-92"><tspan
         id="tspan30642-714"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.192574"
         y="94.642998">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.415127"
       y="94.284737"
       id="text30644-4"><tspan
         id="tspan30642-96"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.415127"
         y="94.284737">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.189857"
       y="94.374306"
       id="text30644-6"><tspan
         id="tspan30642-71"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.189857"
         y="94.374306">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.103004"
       y="89.08992"
       id="text30644-70"><tspan
         id="tspan30642-18"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.103004"
         y="89.08992">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.235996"
       y="89.179489"
       id="text30644-88"><tspan
         id="tspan30642-77"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.235996"
         y="89.179489">X</tspan></text>
    <g
       clip-path="url(#clipEmfPath3)"
       id="g11353"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:140.098%;font-family:Arial;text-align:center;letter-spacing:0px;word-spacing:0px;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(439.37008,1448.1638)"
         x="17.077988"
         y="15.898865"
         id="text11351"><tspan
           x="17.077988"
           y="15.898865"
           id="tspan11345"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan11343">Mal </tspan></tspan><tspan
           x="17.077988"
           y="40.503578"
           id="tspan11349"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan11347">Estado</tspan></tspan></text>
    </g>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.279423"
       y="197.1062"
       id="text30644-85"><tspan
         id="tspan30642-905"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.279423"
         y="197.1062">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="66.923874"
       y="192.89662"
       id="text30644-799"><tspan
         id="tspan30642-56"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="66.923874"
         y="192.89662">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.056866"
       y="192.89662"
       id="text30644-2606"><tspan
         id="tspan30642-07"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.056866"
         y="192.89662">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.100292"
       y="193.34445"
       id="text30644-753"><tspan
         id="tspan30642-213"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.100292"
         y="193.34445">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="66.923874"
       y="188.68703"
       id="text30644-28"><tspan
         id="tspan30642-30"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="66.923874"
         y="188.68703">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="57.9673"
       y="189.04529"
       id="text30644-95"><tspan
         id="tspan30642-85"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="57.9673"
         y="189.04529">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.010727"
       y="188.95573"
       id="text30644-207"><tspan
         id="tspan30642-67"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.010727"
         y="188.95573">X</tspan></text>
    <g
       clip-path="url(#clipEmfPath4)"
       id="g11559"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:140.098%;font-family:Arial;text-align:center;letter-spacing:0px;word-spacing:0px;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(439.37008,1702.4126)"
         x="17.077988"
         y="15.898865"
         id="text11557"><tspan
           x="17.077988"
           y="15.898865"
           id="tspan11551"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan11549">Mal </tspan></tspan><tspan
           x="17.077988"
           y="40.503578"
           id="tspan11555"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan11553">Estado</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath2)"
       id="g11867"
       transform="matrix(0.12936474,0,0,0.12441101,0.87341335,0.14005654)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(507.32598,1712.9575)"
         x="0"
         y="15.898865"
         id="text11565"><tspan
           x="0"
           y="15.898865"
           id="tspan11563"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan11561">N/A</tspan></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:18.75px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(507.32598,1712.9575)"
         x="1.171654"
         y="147.02742"
         id="text11643"><tspan
           x="0"
           y="0"
           id="tspan11641"><tspan
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:18.75px;font-family:Arial;fill:#f2f2f2"
             id="tspan11639" /></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         x="353.85992"
         y="2027.1394"
         id="text11753"><tspan
           x="353.85992"
           y="2027.1394"
           id="tspan11751"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan11747">BUENO</tspan><tspan
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:11.6875px;font-family:Arial;fill:#000000"
             id="tspan11749" /></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         x="511.93515"
         y="2031.9336"
         id="text11759"><tspan
           x="511.93515"
           y="2031.9336"
           id="tspan11757"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan11755">N/A</tspan></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(507.32598,1712.9575)"
         x="-14.059843"
         y="696.87946"
         id="text11855"><tspan
           x="-14.059843"
           y="696.87946"
           id="tspan11853"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan11851">cuales?</tspan></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:146.568%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(507.32598,1712.9575)"
         x="194.49449"
         y="904.26208"
         id="text11865"><tspan
           x="194.49449"
           y="904.26208"
           id="tspan11859"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan11857">Nombre:</tspan></tspan><tspan
           x="194.49449"
           y="926.79907"
           id="tspan11863"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan11861">CC</tspan></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1623.2183"
         y="1906.0547"
         id="text30644-85-89-835"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1623.2183"
           y="1906.0547">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1621.2948"
         y="1950.7648"
         id="text30644-85-89-835-5"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-6"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1621.2948"
           y="1950.7648">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1620.9418"
         y="2036.1907"
         id="text30644-85-89-835-8"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-8"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1620.9418"
           y="2036.1907">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1620.9418"
         y="2080.6687"
         id="text30644-85-89-835-4"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-9"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1620.9418"
           y="2080.6687">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1620.5887"
         y="2121.2637"
         id="text30644-85-89-835-7"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-7"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1620.5887"
           y="2121.2637">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1498.8038"
         y="2122.6758"
         id="text30644-85-89-835-0"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-77"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1498.8038"
           y="2122.6758">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1499.1569"
         y="2076.7856"
         id="text30644-85-89-835-3"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-4"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1499.1569"
           y="2076.7856">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1501.2748"
         y="2031.6017"
         id="text30644-85-89-835-34"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-0"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1501.2748"
           y="2031.6017">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1500.5688"
         y="1948.2937"
         id="text30644-85-89-835-56"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-5"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1500.5688"
           y="1948.2937">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1500.5688"
         y="1902.7567"
         id="text30644-85-89-835-82"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-2"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1500.5688"
           y="1902.7567">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1500.9218"
         y="1861.8088"
         id="text30644-85-89-835-824"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-97"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1500.9218"
           y="1861.8088">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1500.5688"
         y="1818.7428"
         id="text30644-85-89-835-89"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-85"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1500.5688"
           y="1818.7428">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1501.9808"
         y="1776.7358"
         id="text30644-85-89-835-02"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-95"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1501.9808"
           y="1776.7358">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1503.3928"
         y="1734.0228"
         id="text30644-85-89-835-825"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-74"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1503.3928"
           y="1734.0228">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1623.7657"
         y="1862.8678"
         id="text30644-85-89-835-6"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-47"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1623.7657"
           y="1862.8678">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1625.1777"
         y="1822.9788"
         id="text30644-85-89-835-74"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-54"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1625.1777"
           y="1822.9788">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1626.2368"
         y="1776.0298"
         id="text30644-85-89-835-62"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-746"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1626.2368"
           y="1776.0298">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1626.2368"
         y="1733.3168"
         id="text30644-85-89-835-899"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-24"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1626.2368"
           y="1733.3168">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1501.4092"
         y="1658.2655"
         id="text30644-85-89-653"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-46"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1501.4092"
           y="1658.2655">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1502.4077"
         y="1623.3203"
         id="text30644-85-89-35"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-71"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1502.4077"
           y="1623.3203">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1501.4092"
         y="1587.3767"
         id="text30644-85-89-50"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-60"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1501.4092"
           y="1587.3767">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1500.4108"
         y="1551.433"
         id="text30644-85-89-21"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-65"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1500.4108"
           y="1551.433">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1501.4092"
         y="1515.4894"
         id="text30644-85-89-24"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-43"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1501.4092"
           y="1515.4894">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1499.4124"
         y="1485.5364"
         id="text30644-85-89-235"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-42"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1499.4124"
           y="1485.5364">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1623.2183"
         y="1485.5364"
         id="text30644-85-89-68"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-716"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1623.2183"
           y="1485.5364">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1626.2136"
         y="1524.4753"
         id="text30644-85-89-67"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-45"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1626.2136"
           y="1524.4753">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1626.2136"
         y="1556.4252"
         id="text30644-85-89-97"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-91"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1626.2136"
           y="1556.4252">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1623.2183"
         y="1589.3735"
         id="text30644-85-89-98"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-3990"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1623.2183"
           y="1589.3735">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1622.2198"
         y="1623.3203"
         id="text30644-85-89-944"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-70"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1622.2198"
           y="1623.3203">X</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1623.2183"
         y="1657.4445"
         id="text30644-85-89-32"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-72"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1623.2183"
           y="1657.4445">X</tspan></text>
    </g>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.192574"
       y="268.93793"
       id="text30644-85-89-03"><tspan
         id="tspan30642-905-67-95"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.192574"
         y="268.93793">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.235996"
       y="268.93793"
       id="text30644-85-89-089"><tspan
         id="tspan30642-905-67-733"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.235996"
         y="268.93793">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.010727"
       y="269.0275"
       id="text30644-85-89-949"><tspan
         id="tspan30642-905-67-51"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.010727"
         y="269.0275">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.371704"
       y="263.74313"
       id="text30644-85-89-33"><tspan
         id="tspan30642-905-67-69"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.371704"
         y="263.74313">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="57.788166"
       y="264.01181"
       id="text30644-85-89-435"><tspan
         id="tspan30642-905-67-877"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="57.788166"
         y="264.01181">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.461266"
       y="258.36917"
       id="text30644-85-89-432"><tspan
         id="tspan30642-905-67-5"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.461266"
         y="258.36917">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="57.9673"
       y="258.63788"
       id="text30644-85-89-7"><tspan
         id="tspan30642-905-67-92"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="57.9673"
         y="258.63788">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="66.655174"
       y="247.62129"
       id="text30644-85-89-39"><tspan
         id="tspan30642-905-67-85"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="66.655174"
         y="247.62129">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="57.877735"
       y="247.44215"
       id="text30644-85-89-90"><tspan
         id="tspan30642-905-67-35"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="57.877735"
         y="247.44215">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.189857"
       y="247.35258"
       id="text30644-85-89-82"><tspan
         id="tspan30642-905-67-09"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.189857"
         y="247.35258">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.192574"
       y="242.06821"
       id="text30644-85-89-3"><tspan
         id="tspan30642-905-67-87"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.192574"
         y="242.06821">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="57.788166"
       y="242.42647"
       id="text30644-85-89-94"><tspan
         id="tspan30642-905-67-9"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="57.788166"
         y="242.42647">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="57.877735"
       y="236.8734"
       id="text30644-85-89-87"><tspan
         id="tspan30642-905-67-1"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="57.877735"
         y="236.8734">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.235996"
       y="231.49945"
       id="text30644-85-89-8"><tspan
         id="tspan30642-905-67-4"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.235996"
         y="231.49945">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.189857"
       y="231.49945"
       id="text30644-85-89-06"><tspan
         id="tspan30642-905-67-73"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.189857"
         y="231.49945">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.282135"
       y="226.21507"
       id="text30644-85-89-5"><tspan
         id="tspan30642-905-67-7"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.282135"
         y="226.21507">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.111801"
       y="231.51765"
       id="text30644-85-89-5-5"><tspan
         id="tspan30642-905-67-7-8"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.111801"
         y="231.51765">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.238464"
       y="237.13593"
       id="text30644-85-89-5-8"><tspan
         id="tspan30642-905-67-7-0"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.238464"
         y="237.13593">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.235996"
       y="226.21507"
       id="text30644-85-89-0"><tspan
         id="tspan30642-905-67-2"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.235996"
         y="226.21507">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.325562"
       y="220.57243"
       id="text30644-85-89-4"><tspan
         id="tspan30642-905-67-8"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.325562"
         y="220.57243">X</tspan></text>
    <g
       clip-path="url(#clipEmfPath6)"
       id="g11883"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2147.6409)"
         x="0"
         y="12.730408"
         id="text11881"><tspan
           x="0"
           y="12.730408"
           id="tspan11879"><tspan
             dx="0 0"
             dy="0 0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan11877">¿En que estado de Indicador de Nivel?</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath9)"
       id="g11907"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2553.0331)"
         x="0"
         y="11.4375"
         id="text11905"><tspan
           x="0"
           y="11.4375"
           id="tspan11903"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Calibri;fill:#000000"
             id="tspan11901">Galga pico loro                   N°</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath10)"
       id="g11915"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2578.8094)"
         x="0"
         y="11.4375"
         id="text11913"><tspan
           x="0"
           y="11.4375"
           id="tspan11911"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Calibri;fill:#000000"
             id="tspan11909">Cinta Metrica                      N°</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath11)"
       id="g11923"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2604.5858)"
         x="0"
         y="11.4375"
         id="text11921"><tspan
           x="0"
           y="11.4375"
           id="tspan11919"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Calibri;fill:#000000"
             id="tspan11917">Agua Jabonosa                   N°</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath12)"
       id="g11931"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(10.544882,2363.2252)"
         x="0"
         y="12.730408"
         id="text11929"><tspan
           x="0"
           y="12.730408"
           id="tspan11927"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan11925">Tanque Inspeccionado                </tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath13)"
       id="g11939"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2630.3622)"
         x="0"
         y="11.4375"
         id="text11937"><tspan
           x="0"
           y="11.4375"
           id="tspan11935"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Calibri;fill:#000000"
             id="tspan11933">OTRO</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath14)"
       id="g11947"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2394.8598)"
         x="0"
         y="13.80542"
         id="text11945"><tspan
           x="0"
           y="13.80542"
           id="tspan11943"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan11941">Tanque se reporta para ensayo no destructivos</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath15)"
       id="g11991"
       transform="matrix(0.13030134,0,0,0.12421712,1.8810923,-1.5197022)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;line-height:140.098%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2653.7953)"
         x="0"
         y="13.171875"
         id="text11957"><tspan
           x="0"
           y="0"
           id="tspan11951"><tspan
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan11949" /></tspan><tspan
           x="0"
           y="0"
           id="tspan11955"><tspan
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan11953" /></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;line-height:133.427%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2653.7953)"
         x="0"
         y="61.209671"
         id="text11989"><tspan
           x="0"
           y="61.209671"
           id="tspan11961" /><tspan
           x="0"
           y="84.642784"
           id="tspan11967" /><tspan
           x="0"
           y="108.0759"
           id="tspan11975"
           style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;font-family:Calibri;fill:#000000"> </tspan><tspan
           x="0"
           y="131.50902"
           id="tspan11983" /><tspan
           x="0"
           y="154.94214"
           id="tspan11987" /></text>
    </g>
    <g
       clip-path="url(#clipEmfPath16)"
       id="g11999"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2501.4803)"
         x="0"
         y="11.4375"
         id="text11997"><tspan
           x="0"
           y="11.4375"
           id="tspan11995"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Calibri;fill:#000000"
             id="tspan11993">Detector de Fugas             N° </tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath19)"
       id="g12023"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2527.2567)"
         x="0"
         y="11.4375"
         id="text12021"><tspan
           x="0"
           y="11.4375"
           id="tspan12019"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Calibri;fill:#000000"
             id="tspan12017">Multimetro                         N°</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath20)"
       id="g12031"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:italic;font-variant:normal;font-weight:700;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2017.5874)"
         x="0"
         y="12.730408"
         id="text12029"><tspan
           x="0"
           y="12.730408"
           id="tspan12027"><tspan
             dx="0"
             dy="0"
             style="font-style:italic;font-variant:normal;font-weight:700;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12025">REVISION VISUAL DE ACCESORIOS</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath22)"
       id="g12047"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2060.9386)"
         x="0"
         y="12.730408"
         id="text12045"><tspan
           x="0"
           y="12.730408"
           id="tspan12043"><tspan
             dx="0 0"
             dy="0 0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12041">¿En que estado se encuentran las Valvulas?</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath24)"
       id="g12063"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2104.2898)"
         x="0"
         y="12.730408"
         id="text12061"><tspan
           x="0"
           y="12.730408"
           id="tspan12059"><tspan
             dx="0 0"
             dy="0 0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12057">¿En que estado se encuentran las Valvulas alivio?</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath26)"
       id="g12079"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2433.5244)"
         x="0"
         y="13.80542"
         id="text12077"><tspan
           x="0"
           y="13.80542"
           id="tspan12075"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12073">En el momento de la inspeccion se dejan evidencias      Fotograficas                       Video                           Otra  </tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath27)"
       id="g12087"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(60.925984,2469.8457)"
         x="0"
         y="13.171875"
         id="text12085"><tspan
           x="0"
           y="13.171875"
           id="tspan12083"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan12081">EQUIPOS UTILIZADOS</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath28)"
       id="g12095"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(406.56378,2469.8457)"
         x="0"
         y="13.171875"
         id="text12093"><tspan
           x="0"
           y="13.171875"
           id="tspan12091"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan12089">FIRMA DEL INSPECTOR</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath29)"
       id="g12103"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(1103.6976,2469.8457)"
         x="0"
         y="13.171875"
         id="text12101"><tspan
           x="0"
           y="13.171875"
           id="tspan12099"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan12097">FIRMA DEL USUARIO</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath30)"
       id="g12111"
       transform="matrix(0.12840848,0,0,0.12421712,1.7943407,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.5749px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.990664"
         transform="scale(0.99066422,1.0094238)"
         x="953.27893"
         y="2185.0315"
         id="text12109"><tspan
           x="953.27893"
           y="2185.0315"
           id="tspan12107"
           style="stroke-width:0.990664"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.5749px;font-family:Arial;fill:#000000;stroke-width:0.990664"
             id="tspan12105">Numerales exigidos por Resolución 40245 del 2016 De Ministerio De Minas Y Energia</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath31)"
       id="g12119"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(693.6189,2221.4551)"
         x="0"
         y="13.80542"
         id="text12117"><tspan
           x="0"
           y="13.80542"
           id="tspan12115"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12113">OBSERVACIONES Y CONCLUSIONES</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath33)"
       id="g12135"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:18.75px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(738.14173,2337.4488)"
         x="0"
         y="16.973877"
         id="text12133"><tspan
           x="0"
           y="16.973877"
           id="tspan12131"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:18.75px;font-family:Arial;fill:#000000"
             id="tspan12129">Resultado Revisión:</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath34)"
       id="g12143"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(258.93543,2363.2252)"
         x="0"
         y="13.80542"
         id="text12141"><tspan
           x="0"
           y="13.80542"
           id="tspan12139"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12137">CUMPLE</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath35)"
       id="g12151"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(424.13858,2364.3969)"
         x="0"
         y="11.655396"
         id="text12149"><tspan
           x="0"
           y="11.655396"
           id="tspan12147"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;font-family:Arial;fill:#000000"
             id="tspan12145">Numero de Sticker</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath36)"
       id="g12159"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(942.00945,2363.2252)"
         x="0"
         y="13.80542"
         id="text12157"><tspan
           x="0"
           y="13.80542"
           id="tspan12155"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12153">NO CUMPLE</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath38)"
       id="g12175"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,1844.1827)"
         x="0"
         y="12.730408"
         id="text12173"><tspan
           x="0"
           y="12.730408"
           id="tspan12171"><tspan
             dx="0 0"
             dy="0 0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12169">¿La tuberia presenta fisuras y/o escape</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath40)"
       id="g12191"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,1974.2362)"
         x="0"
         y="12.730408"
         id="text12189"><tspan
           x="0"
           y="12.730408"
           id="tspan12187"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12185">¿Los accesorios se encuentran en buen estado?</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath42)"
       id="g12207"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,1930.885)"
         x="0"
         y="12.730408"
         id="text12205"><tspan
           x="0"
           y="12.730408"
           id="tspan12203"><tspan
             dx="0 0"
             dy="0 0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12201">¿Las roscas se encuentran en buen estado?</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath44)"
       id="g12223"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,1887.5339)"
         x="0"
         y="12.730408"
         id="text12221"><tspan
           x="0"
           y="12.730408"
           id="tspan12219"><tspan
             dx="0 0"
             dy="0 0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12217">¿La tuberia presenta aplastamiento o dobleces?</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath46)"
       id="g12239"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:italic;font-variant:normal;font-weight:700;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,1714.1291)"
         x="0"
         y="12.730408"
         id="text12237"><tspan
           x="0"
           y="12.730408"
           id="tspan12235"><tspan
             dx="0"
             dy="0"
             style="font-style:italic;font-variant:normal;font-weight:700;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12233">REVISION VISUAL DE TUBERIA</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath48)"
       id="g12255"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,1757.4803)"
         x="0"
         y="12.730408"
         id="text12253"><tspan
           x="0"
           y="12.730408"
           id="tspan12251"><tspan
             dx="0 0"
             dy="0 0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12249">¿La tuberia presenta defecto de soldadura?</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath50)"
       id="g12271"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,1800.8315)"
         x="0"
         y="12.730408"
         id="text12269"><tspan
           x="0"
           y="12.730408"
           id="tspan12267"><tspan
             dx="0 0"
             dy="0 0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12265">¿La tuberia presenta corrosion?</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath53)"
       id="g12299"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:italic;font-variant:normal;font-weight:700;font-size:14.0625px;line-height:141.64%;font-family:Arial;text-align:center;letter-spacing:0px;word-spacing:0px;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(37.492913,1629.7701)"
         x="30.73082"
         y="12.730408"
         id="text12297"><tspan
           x="30.73082"
           y="12.730408"
           id="tspan12291"><tspan
             dx="0"
             dy="0"
             style="font-style:italic;font-variant:normal;font-weight:700;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12289">ESTADO </tspan></tspan><tspan
           x="32.684326"
           y="32.648533"
           id="tspan12295"><tspan
             dx="0"
             dy="0"
             style="font-style:italic;font-variant:normal;font-weight:700;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12293">GENERAL </tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath54)"
       id="g12307"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1603.9937)"
         x="0"
         y="13.80542"
         id="text12305"><tspan
           x="0"
           y="13.80542"
           id="tspan12303"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12301">Pintura y acabado</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath56)"
       id="g12323"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1639.1433)"
         x="0"
         y="12.730408"
         id="text12321"><tspan
           x="0"
           y="12.730408"
           id="tspan12319"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12317">Protección catódica (enterrados)</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath58)"
       id="g12339"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1674.2929)"
         x="0"
         y="12.730408"
         id="text12337"><tspan
           x="0"
           y="12.730408"
           id="tspan12335"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12333">Continuidad</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath60)"
       id="g12355"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1415.3575)"
         x="0"
         y="13.80542"
         id="text12353"><tspan
           x="0"
           y="13.80542"
           id="tspan12351"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12349">Otros</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath62)"
       id="g12373"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,1458.7087)"
         x="0"
         y="15.898865"
         id="text12371"><tspan
           x="0"
           y="15.898865"
           id="tspan12369"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12365">Estado </tspan><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:12.875px;font-family:Calibri;fill:#000000"
             id="tspan12367">(B=Bueno - M=Mal Estado)</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath63)"
       id="g12381"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(1029.8835,1458.7087)"
         x="0"
         y="15.898865"
         id="text12379"><tspan
           x="0"
           y="15.898865"
           id="tspan12377"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12375">OBSERVACIONES</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath64)"
       id="g12389"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:italic;font-variant:normal;font-weight:700;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(10.544882,1533.6945)"
         x="0"
         y="12.730408"
         id="text12387"><tspan
           x="0"
           y="12.730408"
           id="tspan12385"><tspan
             dx="0"
             dy="0"
             style="font-style:italic;font-variant:normal;font-weight:700;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12383">CRITERIO MTTO</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath65)"
       id="g12397"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1498.5449)"
         x="0"
         y="13.80542"
         id="text12395"><tspan
           x="0"
           y="13.80542"
           id="tspan12393"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12391">Soportes Del Tanque</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath67)"
       id="g12413"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1533.6945)"
         x="0"
         y="13.80542"
         id="text12411"><tspan
           x="0"
           y="13.80542"
           id="tspan12409"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12407">Domo protector o Embebidos</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath69)"
       id="g12429"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1568.8441)"
         x="0"
         y="13.80542"
         id="text12427"><tspan
           x="0"
           y="13.80542"
           id="tspan12425"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12423">Orejas de izamiento</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath70)"
       id="g12443"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(25.776378,1234.9228)"
         x="0"
         y="11.655396"
         id="text12435"><tspan
           x="0"
           y="11.655396"
           id="tspan12433"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;font-family:Arial;fill:#000000"
             id="tspan12431">Numeral 10,3                  </tspan></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(25.776378,1234.9228)"
         x="15.231496"
         y="30.401852"
         id="text12441"><tspan
           x="15.231496"
           y="30.401852"
           id="tspan12439"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;font-family:Arial;fill:#000000"
             id="tspan12437">Literal g</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath71)"
       id="g12451"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1241.9528)"
         x="0"
         y="13.80542"
         id="text12449"><tspan
           x="0"
           y="13.80542"
           id="tspan12447"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12445">Accion por Fuego</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath72)"
       id="g12463"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:138.294%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(557.70709,1232.5795)"
         x="0"
         y="13.80542"
         id="text12461"><tspan
           x="0"
           y="13.80542"
           id="tspan12455"><tspan
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12453">Ha soportado temperaturas excesivas                                                                                                                              </tspan></tspan><tspan
           x="0"
           y="34.895256"
           id="tspan12459"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12457">Tiene variacion en su geometria original</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath73)"
       id="g12481"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:14.0625px;line-height:141.64%;font-family:Arial;text-align:center;letter-spacing:0px;word-spacing:0px;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(39.83622,1333.3417)"
         x="30.73082"
         y="12.730408"
         id="text12473"><tspan
           x="30.73082"
           y="12.730408"
           id="tspan12467"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12465">ESTADO </tspan></tspan><tspan
           x="30.73082"
           y="32.648533"
           id="tspan12471"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12469">CONEXIONES</tspan></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(39.83622,1333.3417)"
         x="-31.634645"
         y="49.49247"
         id="text12479"><tspan
           x="-31.634645"
           y="49.49247"
           id="tspan12477"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;font-family:Calibri;fill:#000000"
             id="tspan12475">numeral 10,3 literal h</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath74)"
       id="g12489"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1285.3039)"
         x="0"
         y="13.80542"
         id="text12487"><tspan
           x="0"
           y="13.80542"
           id="tspan12485"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12483">Corrosión</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath76)"
       id="g12505"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1328.6551)"
         x="0"
         y="13.80542"
         id="text12503"><tspan
           x="0"
           y="13.80542"
           id="tspan12501"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12499">Evidencia de Golpes</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath78)"
       id="g12521"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1372.0063)"
         x="0"
         y="13.80542"
         id="text12519"><tspan
           x="0"
           y="13.80542"
           id="tspan12517"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12515">Desgaste</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath80)"
       id="g12539"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:italic;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,1043.9433)"
         x="0"
         y="13.80542"
         id="text12537"><tspan
           x="0"
           y="13.80542"
           id="tspan12535"><tspan
             dx="0"
             dy="0"
             style="font-style:italic;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12531">ABOMBAMIENTO </tspan><tspan
             dx="-0.61917198"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:12.875px;font-family:Calibri;fill:#000000"
             id="tspan12533">  numeral 10,3 literal c</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath81)"
       id="g12547"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(557.70709,1043.9433)"
         x="0"
         y="13.80542"
         id="text12545"><tspan
           x="0"
           y="13.80542"
           id="tspan12543"><tspan
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12541">Presenta abombamiento visible definido</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath82)"
       id="g12565"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:14.0625px;line-height:135.132%;font-family:Calibri;text-align:center;letter-spacing:0px;word-spacing:0px;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(31.634646,1121.2724)"
         x="37.271118"
         y="10.546875"
         id="text12557"><tspan
           x="37.271118"
           y="10.546875"
           id="tspan12551"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:14.0625px;font-family:Calibri;fill:#000000"
             id="tspan12549">CORROSIÓN </tspan></tspan><tspan
           x="39.256332"
           y="30.424812"
           id="tspan12555"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan12553">numeral 10,3 </tspan></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(31.634646,1121.2724)"
         x="-4.686614"
         y="56.523056"
         id="text12563"><tspan
           x="-4.686614"
           y="56.523056"
           id="tspan12561"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan12559">literal d,e,f</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath83)"
       id="g12573"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1087.2945)"
         x="0"
         y="13.80542"
         id="text12571"><tspan
           x="0"
           y="13.80542"
           id="tspan12569"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12567">Corrosión aislada</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath84)"
       id="g12585"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:138.294%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(557.70709,1077.9213)"
         x="0"
         y="13.80542"
         id="text12583"><tspan
           x="0"
           y="13.80542"
           id="tspan12577"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12575">Presenta picadura aislada de una profundidad &gt; 15% del espesor                                                                      </tspan></tspan><tspan
           x="0"
           y="34.895256"
           id="tspan12581"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12579">El espesor de pared remanente es inferior a 3,18 mm </tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath85)"
       id="g12593"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1143.5339)"
         x="0"
         y="13.80542"
         id="text12591"><tspan
           x="0"
           y="13.80542"
           id="tspan12589"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12587">Corrosión en línea</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath86)"
       id="g12611"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:138.294%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(557.70709,1123.6157)"
         x="0"
         y="13.80542"
         id="text12603"><tspan
           x="0"
           y="13.80542"
           id="tspan12597"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12595">Corrosion en linea con longitud &gt; de 76mm                                                                                                                                                              </tspan></tspan><tspan
           x="0"
           y="34.895256"
           id="tspan12601"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12599">Profundidad de picadura &gt; al 15% de espesor                                                                                                                                                                   </tspan></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(557.70709,1123.6157)"
         x="0"
         y="54.813293"
         id="text12609"><tspan
           x="0"
           y="54.813293"
           id="tspan12607"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12605">El espesor de pared remanente es inferior a 3,18 mm       </tspan></tspan></text>
    </g>
    <g
       id="g15703-5-1-4-76-5"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,82.543051,79.192371)">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-1" />
      <g
         id="g15698-7-9-3-10-2"
         style="stroke:#000000;stroke-opacity:1">
        <path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-0" />
      </g>
    </g>
    <g
       id="g15703-5-1-4-76-54"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,82.543051,81.599008)">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-6" />
      <g
         id="g15698-7-9-3-10-9"
         style="stroke:#000000;stroke-opacity:1">
        <path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-1" />
      </g>
    </g>
    <g
       id="g15703-5-1-4-76-7"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,82.479718,84.195643)">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-7" />
      <g
         id="g15698-7-9-3-10-5"
         style="stroke:#000000;stroke-opacity:1">
        <path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-2" />
      </g>
    </g>
    <g
       clip-path="url(#clipEmfPath87)"
       id="g12619"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1198.6016)"
         x="0"
         y="13.80542"
         id="text12617"><tspan
           x="0"
           y="13.80542"
           id="tspan12615"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12613">Corrosión general</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath88)"
       id="g12631"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:138.294%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(557.70709,1189.2283)"
         x="0"
         y="13.80542"
         id="text12629"><tspan
           x="0"
           y="13.80542"
           id="tspan12623"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12621">Profundidad de picadura &gt; al 15% de espesor                                                                                                                                            </tspan></tspan><tspan
           x="0"
           y="34.895256"
           id="tspan12627"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12625">El espesor de pared remanente es inferior a 3,18 mm</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath89)"
       id="g12639"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,870.53858)"
         x="0"
         y="13.80542"
         id="text12637"><tspan
           x="0"
           y="13.80542"
           id="tspan12635"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12633">Socavado</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath91)"
       id="g12657"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:italic;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,957.24094)"
         x="0"
         y="13.80542"
         id="text12655"><tspan
           x="0"
           y="13.80542"
           id="tspan12653"><tspan
             dx="0"
             dy="0"
             style="font-style:italic;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12649">ABOLLADURA </tspan><tspan
             dx="0.65633702"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:12.875px;font-family:Calibri;fill:#000000"
             id="tspan12651"> numeral 10,3 literal b</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath92)"
       id="g12665"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(557.70709,913.88976)"
         x="0"
         y="13.80542"
         id="text12663"><tspan
           x="0"
           y="13.80542"
           id="tspan12661"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12659">Compromete un zona de soldadura</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath93)"
       id="g12677"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:138.294%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(557.70709,947.86772)"
         x="0"
         y="13.80542"
         id="text12675"><tspan
           x="0"
           y="13.80542"
           id="tspan12669"><tspan
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12667">Se encuentra en la zona afectada por el calor de una soldadura                                                                                                                                                                                                                                       </tspan></tspan><tspan
           x="0"
           y="34.895256"
           id="tspan12673"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12671">( dis. A 3 cm a partir de la soldadura)</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath94)"
       id="g12685"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(557.70709,1000.5921)"
         x="0"
         y="13.80542"
         id="text12683"><tspan
           x="0"
           y="13.80542"
           id="tspan12681"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12679">Su profundidad exceda de 6,35 mm o 1/10 de diametro promedio                                             de la abolladura</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath95)"
       id="g12693"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(14.059843,697.13386)"
         x="0"
         y="15.898865"
         id="text12691"><tspan
           x="0"
           y="15.898865"
           id="tspan12689"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12687">Numeral 10.1</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath96)"
       id="g12701"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,697.13386)"
         x="0"
         y="15.898865"
         id="text12699"><tspan
           x="0"
           y="15.898865"
           id="tspan12697"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12695">Hermeticidad</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath97)"
       id="g12709"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(557.70709,697.13386)"
         x="0"
         y="13.80542"
         id="text12707"><tspan
           x="0"
           y="13.80542"
           id="tspan12705"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12703">Presenta fisuras/escape </tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath98)"
       id="g12727"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:14.0625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(29.291339,785.00787)"
         x="0"
         y="10.546875"
         id="text12715"><tspan
           x="0"
           y="10.546875"
           id="tspan12713"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:14.0625px;font-family:Calibri;fill:#000000"
             id="tspan12711">SOLDADURA         </tspan></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:133.427%;font-family:Calibri;text-align:center;letter-spacing:0px;word-spacing:0px;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(29.291339,785.00787)"
         x="40.814529"
         y="34.261639"
         id="text12725"><tspan
           x="40.814529"
           y="34.261639"
           id="tspan12719"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan12717">numeral 10,3 </tspan></tspan><tspan
           x="40.814529"
           y="57.694756"
           id="tspan12723"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan12721">literal a</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath99)"
       id="g12735"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,740.48504)"
         x="0"
         y="13.80542"
         id="text12733"><tspan
           x="0"
           y="13.80542"
           id="tspan12731"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12729">Agrietamiento</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath101)"
       id="g12751"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,783.83622)"
         x="0"
         y="13.80542"
         id="text12749"><tspan
           x="0"
           y="13.80542"
           id="tspan12747"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12745">Porosidad</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath103)"
       id="g12767"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,827.1874)"
         x="0"
         y="13.80542"
         id="text12765"><tspan
           x="0"
           y="13.80542"
           id="tspan12763"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12761">Salpicadura</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath104)"
       id="g12775"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(557.70709,827.1874)"
         x="0"
         y="13.80542"
         id="text12773"><tspan
           x="0"
           y="13.80542"
           id="tspan12771"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12769"> </tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath105)"
       id="g12783"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,622.14803)"
         x="0"
         y="13.80542"
         id="text12781"><tspan
           x="0"
           y="13.80542"
           id="tspan12779"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12777">CLASE DE USUARIO</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath106)"
       id="g12791"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(636.20787,622.14803)"
         x="0"
         y="15.898865"
         id="text12789"><tspan
           x="0"
           y="15.898865"
           id="tspan12787"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12785">Residencial                    Comercial                        Industrial                               </tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath107)"
       id="g12799"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(78.500787,654.95433)"
         x="0"
         y="15.898865"
         id="text12797"><tspan
           x="0"
           y="15.898865"
           id="tspan12795"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12793">REQUISITO A EVALUAR</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath108)"
       id="g12807"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(405.39213,645.5811)"
         x="0"
         y="13.80542"
         id="text12805"><tspan
           x="0"
           y="13.80542"
           id="tspan12803"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12801">¿PRESENTA?</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath109)"
       id="g12815"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(917.40472,654.95433)"
         x="0"
         y="15.898865"
         id="text12813"><tspan
           x="0"
           y="15.898865"
           id="tspan12811"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12809">DEFECTOLOGIA</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath110)"
       id="g12823"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(1441.1339,654.95433)"
         x="0"
         y="15.898865"
         id="text12821"><tspan
           x="0"
           y="15.898865"
           id="tspan12819"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12817">CUMPLE</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath111)"
       id="g12831"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(1543.0677,654.95433)"
         x="0"
         y="15.898865"
         id="text12829"><tspan
           x="0"
           y="15.898865"
           id="tspan12827"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12825">NO CUMPLE</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath114)"
       id="g12855"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(1120.1008,362.04095)"
         x="0"
         y="15.898865"
         id="text12853"><tspan
           x="0"
           y="15.898865"
           id="tspan12851"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12849">IDENTIFICACIÓN DEL TANQUE</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath115)"
       id="g12863"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,451.08661)"
         x="0"
         y="15.898865"
         id="text12861"><tspan
           x="0"
           y="15.898865"
           id="tspan12859"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12857">Teléfono:</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath116)"
       id="g12871"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,495.60945)"
         x="0"
         y="15.898865"
         id="text12869"><tspan
           x="0"
           y="15.898865"
           id="tspan12867"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12865">Contacto:</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath117)"
       id="g12879"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,595.2)"
         x="0"
         y="13.80542"
         id="text12877"><tspan
           x="0"
           y="13.80542"
           id="tspan12875"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12873">TIPO DE TANQUE</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath118)"
       id="g12887"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         x="320.48694"
         y="609.00543"
         id="text12885"><tspan
           x="320.48694"
           y="609.00543"
           id="tspan12883"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12881">HORIZONTAL</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath119)"
       id="g12895"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(597.54331,599.88661)"
         x="0"
         y="13.80542"
         id="text12893"><tspan
           x="0"
           y="13.80542"
           id="tspan12891"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12889">SUPERFICIAL</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath120)"
       id="g12903"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(1050.9732,595.2)"
         x="0"
         y="13.80542"
         id="text12901"><tspan
           x="0"
           y="13.80542"
           id="tspan12899"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12897">CARCAMO</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath123)"
       id="g12927"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(796.72441,4.686614)"
         x="0"
         y="16.973877"
         id="text12925"><tspan
           x="0"
           y="16.973877"
           id="tspan12923"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;font-family:Arial;fill:#404040"
             id="tspan12921">NIT. 901.356.384 – 1</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath124)"
       id="g12935"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(686.58898,30.462992)"
         x="0"
         y="16.973877"
         id="text12933"><tspan
           x="0"
           y="16.973877"
           id="tspan12931"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;font-family:Arial;fill:#404040"
             id="tspan12929">Carrera 13ª N° 28 – 38 oficina 241 C.E Bavaria </tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath125)"
       id="g12943"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(785.00787,51.552756)"
         x="0"
         y="16.973877"
         id="text12941"><tspan
           x="0"
           y="16.973877"
           id="tspan12939"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;font-family:Arial;fill:#404040"
             id="tspan12937">Teléfonos 3133184230 </tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath126)"
       id="g12951"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(640.89449,74.985827)"
         x="0"
         y="16.973877"
         id="text12949"><tspan
           x="0"
           y="16.973877"
           id="tspan12947"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;font-family:Arial;fill:#404040"
             id="tspan12945">Email:  gerencia@qcsas.com; director.tecnico@qcsas.com</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath127)"
       id="g12959"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(1347.4016,4.686614)"
         x="0"
         y="16.973877"
         id="text12957"><tspan
           x="0"
           y="16.973877"
           id="tspan12955"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;font-family:Arial;fill:#404040"
             id="tspan12953">CODIGO: SGQC-PGT-FT-03</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath128)"
       id="g12967"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(1413.0142,30.462992)"
         x="0"
         y="16.973877"
         id="text12965"><tspan
           x="0"
           y="16.973877"
           id="tspan12963"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;font-family:Arial;fill:#404040"
             id="tspan12961">EDICION: 01</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath129)"
       id="g12975"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(1381.3795,51.552756)"
         x="0"
         y="16.973877"
         id="text12973"><tspan
           x="0"
           y="16.973877"
           id="tspan12971"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;font-family:Arial;fill:#404040"
             id="tspan12969">FECHA: 2022-02-01</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath130)"
       id="g12983"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(1329.8268,86.702362)"
         x="0"
         y="16.973877"
         id="text12981"><tspan
           x="0"
           y="16.973877"
           id="tspan12979"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;font-family:Arial;fill:#0070c0"
             id="tspan12977">REVISION PARCIAL N° 0000</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath131)"
       id="g12991"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(813.12756,98.418898)"
         x="0"
         y="13.171875"
         id="text12989"><tspan
           x="0"
           y="13.171875"
           id="tspan12987"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;font-family:Calibri;fill:#0563c1"
             id="tspan12985">WWW.QCSAS.COM</tspan></tspan></text>
    </g>
    <path
       style="fill:#0563c1;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath131)"
       d="m 813.12756,117.16535 h 138.25512 v 1.17166 H 813.12756 Z"
       id="path12993"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <g
       clip-path="url(#clipEmfPath132)"
       id="g13001"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,534.27402)"
         x="0"
         y="15.898865"
         id="text12999"><tspan
           x="0"
           y="15.898865"
           id="tspan12997"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12995">CRITERIOS DE INSPECCION: Resolucion 40245 del 16 de marzo del 2016 Numeral 10.1 y 10.3 de Ministerio de Minas y Energia</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath133)"
       id="g13009"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(24.604724,565.90866)"
         x="0"
         y="15.898865"
         id="text13007"><tspan
           x="0"
           y="15.898865"
           id="tspan13005"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan13003">Ubicación </tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath134)"
       id="g13017"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(523.72913,565.90866)"
         x="0"
         y="15.898865"
         id="text13015"><tspan
           x="0"
           y="15.898865"
           id="tspan13013"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan13011">Revisión</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath136)"
       id="g13033"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(1470.4252,406.56378)"
         x="0"
         y="15.898865"
         id="text13031"><tspan
           x="0"
           y="15.898865"
           id="tspan13029"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan13027">galones de agua</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath137)"
       id="g13041"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(913.88976,407.73543)"
         x="0"
         y="13.80542"
         id="text13039"><tspan
           x="0"
           y="13.80542"
           id="tspan13037"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan13035">Capacidad Nominal</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath138)"
       id="g13049"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(922.09134,496.7811)"
         x="0"
         y="13.80542"
         id="text13047"><tspan
           x="0"
           y="13.80542"
           id="tspan13045"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan13043">Número de Serie:</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath139)"
       id="g13057"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,317.51811)"
         x="0"
         y="15.898865"
         id="text13055"><tspan
           x="0"
           y="15.898865"
           id="tspan13053"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan13051">NIT o C.C:</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath140)"
       id="g13065"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,362.04095)"
         x="0"
         y="15.898865"
         id="text13063"><tspan
           x="0"
           y="15.898865"
           id="tspan13061"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan13059">Usuario:</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath141)"
       id="g13073"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,406.56378)"
         x="0"
         y="15.898865"
         id="text13071"><tspan
           x="0"
           y="15.898865"
           id="tspan13069"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan13067">Dirección:</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath143)"
       id="g13089"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(945.52441,452.25827)"
         x="0"
         y="13.80542"
         id="text13087"><tspan
           x="0"
           y="13.80542"
           id="tspan13085"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan13083">Fabricante:</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath145)"
       id="g13105"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,220.27087)"
         x="0"
         y="13.171875"
         id="text13103"><tspan
           x="0"
           y="13.171875"
           id="tspan13101"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan13099">FECHA DE INSPECCION: </tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath146)"
       id="g13113"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:24.625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(697.13386,144.11339)"
         x="0"
         y="18.46875"
         id="text13111"><tspan
           x="0"
           y="18.46875"
           id="tspan13109"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:24.625px;font-family:Calibri;fill:#000000"
             id="tspan13107">INFORME DE INSPECCION</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath147)"
       id="g13121"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:24.625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(522.55748,176.91968)"
         x="0"
         y="18.46875"
         id="text13119"><tspan
           x="0"
           y="18.46875"
           id="tspan13117"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:24.625px;font-family:Calibri;fill:#000000"
             id="tspan13115">REVISION PARCIAL DE TANQUES ESTACIONARIOS PARA GLP</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath148)"
       id="g13129"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:22.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(988.87559,217.92756)"
         x="0"
         y="20.142334"
         id="text13127"><tspan
           x="0"
           y="20.142334"
           id="tspan13125"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:22.25px;font-family:Arial;fill:#000000"
             id="tspan13123">DATOS DEL CLIENTE</tspan></tspan></text>
    </g>
    <g
       clip-path="url(#clipEmfPath149)"
       id="g13137"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,267.13701)"
         x="0"
         y="15.898865"
         id="text13135"><tspan
           x="0"
           y="15.898865"
           id="tspan13133"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan13131">Propietario:</tspan></tspan></text>
    </g>
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 0,0 V 209.72598"
       id="path13155"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 0,0 H 1.1716535 V 209.72598 H 0 Z"
       id="path13157"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1655.5465,1.1716535 V 209.72598"
       id="path13159"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,1.1716535 h 1.1716 V 209.72598 h -1.1716 z"
       id="path13161"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,249.5622 H 553.02047"
       id="path13163"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,249.5622 H 553.02047 v 1.17166 H 1.1716535 Z"
       id="path13165"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 133.5685,250.73386 V 529.5874"
       id="path13167"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 133.5685,250.73386 h 1.17166 V 529.5874 h -1.17166 z"
       id="path13169"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 842.4189,351.49606 V 529.5874"
       id="path13171"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 842.4189,351.49606 h 1.17165 V 529.5874 h -1.17165 z"
       id="path13173"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1130.6457,396.0189 V 529.5874"
       id="path13175"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1130.6457,396.0189 h 1.1716 v 133.5685 h -1.1716 z"
       id="path13177"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1418.8724,396.0189 v 44.52283"
       id="path13179"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1418.8724,396.0189 h 1.1717 v 44.52283 h -1.1717 z"
       id="path13181"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 353.83937,561.22205 v 31.63464"
       id="path13183"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 353.83937,561.22205 h 1.17165 v 31.63464 h -1.17165 z"
       id="path13185"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 553.02047,212.06929 h 2.34331 v 38.66457 h -2.34331 z"
       id="path13187"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1418.8724,561.22205 v 58.58267"
       id="path13189"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1418.8724,561.22205 h 1.1717 v 58.58267 h -1.1717 z"
       id="path13191"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1537.2094,561.22205 v 58.58267"
       id="path13193"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1537.2094,561.22205 h 1.1717 v 58.58267 h -1.1717 z"
       id="path13195"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 420.62362,561.22205 v 58.58267"
       id="path13197"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 420.62362,561.22205 h 1.17166 v 58.58267 h -1.17166 z"
       id="path13199"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 487.40787,592.85669 v 26.94803"
       id="path13201"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 487.40787,592.85669 h 1.17166 v 26.94803 h -1.17166 z"
       id="path13203"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 133.5685,561.22205 v 58.58267"
       id="path13205"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 133.5685,561.22205 h 1.17166 v 58.58267 h -1.17166 z"
       id="path13207"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 133.5685,686.58898 v 216.7559"
       id="path13209"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 133.5685,686.58898 h 1.17166 v 216.7559 h -1.17166 z"
       id="path13211"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 133.5685,1076.7496 v 371.4142"
       id="path13213"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 133.5685,1076.7496 h 1.17166 v 371.4142 h -1.17166 z"
       id="path13215"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1418.8724,646.75276 V 1448.1638"
       id="path13217"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1418.8724,646.75276 h 1.1717 v 801.41104 h -1.1717 z"
       id="path13219"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1537.2094,646.75276 V 1448.1638"
       id="path13221"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1537.2094,646.75276 h 1.1717 v 801.41104 h -1.1717 z"
       id="path13223"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1418.8724,1491.515 v 210.8976"
       id="path13225"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1418.8724,1491.515 h 1.1717 v 210.8976 h -1.1717 z"
       id="path13227"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1537.2094,1491.515 v 210.8976"
       id="path13229"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1537.2094,1491.515 h 1.1717 v 210.8976 h -1.1717 z"
       id="path13231"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1418.8724,1745.7638 v 260.1071"
       id="path13233"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1418.8724,1745.7638 h 1.1717 v 260.1071 h -1.1717 z"
       id="path13235"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1537.2094,1745.7638 v 260.1071"
       id="path13237"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1537.2094,1745.7638 h 1.1717 v 260.1071 h -1.1717 z"
       id="path13239"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 0,212.06929 V 2217.9402"
       id="path13241"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 0,212.06929 H 1.1716535 V 2217.9402 H 0 Z"
       id="path13243"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1655.5465,212.06929 V 2217.9402"
       id="path13245"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,212.06929 h 1.1716 V 2217.9402 h -1.1716 z"
       id="path13247"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2220.2835 v 21.0897"
       id="path13249"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2220.2835 h 1.1716535 v 21.0897 H 0 Z"
       id="path13251"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2220.2835 v 21.0897"
       id="path13253"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2220.2835 h 1.1716 v 21.0897 h -1.1716 z"
       id="path13255"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2243.7165 v 91.389"
       id="path13257"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2243.7165 h 1.1716535 v 91.389 H 0 Z"
       id="path13259"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2243.7165 v 91.389"
       id="path13261"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2243.7165 h 1.1716 v 91.389 h -1.1716 z"
       id="path13263"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2337.4488 v 21.0898"
       id="path13265"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2337.4488 h 1.1716535 v 21.0898 H 0 Z"
       id="path13267"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 353.83937,646.75276 V 2179.2756"
       id="path13269"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 353.83937,646.75276 h 1.17165 V 2179.2756 h -1.17165 z"
       id="path13271"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 420.62362,666.67087 V 2179.2756"
       id="path13273"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 420.62362,666.67087 h 1.17166 V 2179.2756 h -1.17166 z"
       id="path13275"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 842.4189,561.22205 v 58.58267"
       id="path13277"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 842.4189,561.22205 h 1.17165 v 58.58267 h -1.17165 z"
       id="path13279"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1130.6457,561.22205 v 58.58267"
       id="path13281"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1130.6457,561.22205 h 1.1716 v 58.58267 h -1.1716 z"
       id="path13283"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1274.7591,561.22205 v 58.58267"
       id="path13285"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1274.7591,561.22205 h 1.1716 v 58.58267 h -1.1716 z"
       id="path13287"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2337.4488 v 21.0898"
       id="path13289"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2337.4488 h 1.1716 v 21.0898 h -1.1716 z"
       id="path13291"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2360.8819 v 23.4331"
       id="path13293"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2360.8819 h 1.1716535 v 23.4331 H 0 Z"
       id="path13295"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 487.40787,666.67087 V 2179.2756"
       id="path13297"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 487.40787,666.67087 h 1.17166 V 2179.2756 h -1.17166 z"
       id="path13299"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2360.8819 v 23.4331"
       id="path13301"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2360.8819 h 1.1716 v 23.4331 h -1.1716 z"
       id="path13303"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2386.6583 v 36.3212"
       id="path13305"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2386.6583 h 1.1716535 v 36.3212 H 0 Z"
       id="path13307"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2386.6583 v 36.3212"
       id="path13309"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2386.6583 h 1.1716 v 36.3212 h -1.1716 z"
       id="path13311"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2425.3228 v 36.3213"
       id="path13313"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2425.3228 h 1.1716535 v 36.3213 H 0 Z"
       id="path13315"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 274.16693,561.22205 v 58.58267"
       id="path13317"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 274.16693,561.22205 h 1.17165 v 58.58267 h -1.17165 z"
       id="path13319"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 698.30551,561.22205 v 58.58267"
       id="path13321"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 698.30551,561.22205 h 1.17166 v 58.58267 h -1.17166 z"
       id="path13323"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2425.3228 v 36.3213"
       id="path13325"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2425.3228 h 1.1716 v 36.3213 h -1.1716 z"
       id="path13327"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2463.9874 v 31.6346"
       id="path13329"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2463.9874 h 1.1716535 v 31.6346 H 0 Z"
       id="path13331"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2463.9874 v 31.6346"
       id="path13333"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2463.9874 h 1.1716 v 31.6346 h -1.1716 z"
       id="path13335"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2497.9654 v 23.433"
       id="path13337"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2497.9654 h 1.1716535 v 23.433 H 0 Z"
       id="path13339"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2523.7417 v 23.4331"
       id="path13341"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2523.7417 h 1.1716535 v 23.4331 H 0 Z"
       id="path13343"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2549.5181 v 23.4331"
       id="path13345"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2549.5181 h 1.1716535 v 23.4331 H 0 Z"
       id="path13347"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2575.2945 v 23.4331"
       id="path13349"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2575.2945 h 1.1716535 v 23.4331 H 0 Z"
       id="path13351"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2598.7276 h 275.33858 v 2.3433 H 0 Z"
       id="path13353"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 841.24724,2360.8819 h 2.34331 v 25.7764 h -2.34331 z"
       id="path13355"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2497.9654 v 100.7622"
       id="path13357"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2497.9654 h 1.1716 v 100.7622 h -1.1716 z"
       id="path13359"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2601.0709 v 23.433"
       id="path13361"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2601.0709 h 1.1716535 v 23.433 H 0 Z"
       id="path13363"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2624.5039 h 275.33858 v 2.3433 H 0 Z"
       id="path13365"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2626.8472 v 23.4331"
       id="path13367"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2626.8472 h 1.1716535 v 23.4331 H 0 Z"
       id="path13369"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2601.0709 v 49.2094"
       id="path13371"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2601.0709 h 1.1716 v 49.2094 h -1.1716 z"
       id="path13373"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2652.6236 v 209.726"
       id="path13375"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2652.6236 h 1.1716535 v 209.726 H 0 Z"
       id="path13377"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2652.6236 v 209.726"
       id="path13379"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2652.6236 h 1.1716 v 209.726 h -1.1716 z"
       id="path13381"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 554.19213,646.75276 V 2179.2756"
       id="path13383"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 554.19213,646.75276 h 1.17165 V 2179.2756 h -1.17165 z"
       id="path13385"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.534149"
       y="93.567505"
       id="text2073-3"><tspan
         id="tspan2071-6"
         style="stroke-width:0.557"
         x="75.534149"
         y="93.567505">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.416817"
       y="99.105446"
       id="text2073-34"><tspan
         id="tspan2071-67"
         style="stroke-width:0.557"
         x="75.416817"
         y="99.105446">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.416817"
       y="104.36465"
       id="text2073-8"><tspan
         id="tspan2071-3"
         style="stroke-width:0.557"
         x="75.416817"
         y="104.36465">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.416817"
       y="109.87431"
       id="text2073-4"><tspan
         id="tspan2071-9"
         style="stroke-width:0.557"
         x="75.416817"
         y="109.87431">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="106.93966"
       y="115.38396"
       id="text2073-31"><tspan
         id="tspan2071-0"
         style="stroke-width:0.557"
         x="106.93966"
         y="115.38396">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="131.95941"
       y="120.36444"
       id="text2073-5"><tspan
         id="tspan2071-1"
         style="stroke-width:0.557"
         x="131.95941"
         y="120.36444">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="132.18156"
       y="125.87409"
       id="text2073-46"><tspan
         id="tspan2071-7"
         style="stroke-width:0.557"
         x="132.18156"
         y="125.87409">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="112.78462"
       y="131.16159"
       id="text2073-1"><tspan
         id="tspan2071-37"
         style="stroke-width:0.557"
         x="112.78462"
         y="131.16159">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="133.54279"
       y="135.39078"
       id="text2073-47"><tspan
         id="tspan2071-03"
         style="stroke-width:0.557"
         x="133.54279"
         y="135.39078">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="124.93887"
       y="138.42432"
       id="text2073-51"><tspan
         id="tspan2071-4"
         style="stroke-width:0.557"
         x="124.93887"
         y="138.42432">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="116.12518"
       y="141.17914"
       id="text2073-2"><tspan
         id="tspan2071-35"
         style="stroke-width:0.557"
         x="116.12518"
         y="141.17914">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="116.64228"
       y="144.05919"
       id="text2073-58"><tspan
         id="tspan2071-671"
         style="stroke-width:0.557"
         x="116.64228"
         y="144.05919">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="122.02671"
       y="146.43837"
       id="text2073-89"><tspan
         id="tspan2071-42"
         style="stroke-width:0.557"
         x="122.02671"
         y="146.43837">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="119.27189"
       y="149.31841"
       id="text2073-13"><tspan
         id="tspan2071-31"
         style="stroke-width:0.557"
         x="119.27189"
         y="149.31841">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="122.02671"
       y="152.07323"
       id="text2073-6"><tspan
         id="tspan2071-60"
         style="stroke-width:0.557"
         x="122.02671"
         y="152.07323">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="110.13087"
       y="154.70284"
       id="text2073-85"><tspan
         id="tspan2071-04"
         style="stroke-width:0.557"
         x="110.13087"
         y="154.70284">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="110.50652"
       y="157.45766"
       id="text2073-83"><tspan
         id="tspan2071-2"
         style="stroke-width:0.557"
         x="110.50652"
         y="157.45766">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.138092"
       y="161.71512"
       id="text2073-517"><tspan
         id="tspan2071-5"
         style="stroke-width:0.557"
         x="75.138092"
         y="161.71512">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.138092"
       y="167.22478"
       id="text2073-80"><tspan
         id="tspan2071-78"
         style="stroke-width:0.557"
         x="75.138092"
         y="167.22478">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.166382"
       y="172.23355"
       id="text2073-50"><tspan
         id="tspan2071-38"
         style="stroke-width:0.557"
         x="75.166382"
         y="172.23355">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.416817"
       y="177.46448"
       id="text2073-0"><tspan
         id="tspan2071-08"
         style="stroke-width:0.557"
         x="75.416817"
         y="177.46448">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.388527"
       y="187.76074"
       id="text2073-9"><tspan
         id="tspan2071-29"
         style="stroke-width:0.557"
         x="75.388527"
         y="187.76074">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.416817"
       y="192.54736"
       id="text2073-95"><tspan
         id="tspan2071-99"
         style="stroke-width:0.557"
         x="75.416817"
         y="192.54736">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.416817"
       y="196.52609"
       id="text2073-86"><tspan
         id="tspan2071-8"
         style="stroke-width:0.557"
         x="75.416817"
         y="196.52609">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.416817"
       y="200.78355"
       id="text2073-589"><tspan
         id="tspan2071-316"
         style="stroke-width:0.557"
         x="75.416817"
         y="200.78355">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.667259"
       y="205.79233"
       id="text2073-49"><tspan
         id="tspan2071-01"
         style="stroke-width:0.557"
         x="75.667259"
         y="205.79233">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.667259"
       y="209.77107"
       id="text2073-7"><tspan
         id="tspan2071-44"
         style="stroke-width:0.557"
         x="75.667259"
         y="209.77107">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.138092"
       y="219.81689"
       id="text2073-18"><tspan
         id="tspan2071-449"
         style="stroke-width:0.557"
         x="75.138092"
         y="219.81689">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.138092"
       y="225.32655"
       id="text2073-10"><tspan
         id="tspan2071-27"
         style="stroke-width:0.557"
         x="75.138092"
         y="225.32655">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.138092"
       y="230.08488"
       id="text2073-79"><tspan
         id="tspan2071-25"
         style="stroke-width:0.557"
         x="75.138092"
         y="230.08488">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.166382"
       y="235.3441"
       id="text2073-43"><tspan
         id="tspan2071-97"
         style="stroke-width:0.557"
         x="75.166382"
         y="235.3441">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.166382"
       y="240.85374"
       id="text2073-70"><tspan
         id="tspan2071-447"
         style="stroke-width:0.557"
         x="75.166382"
         y="240.85374">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.445107"
       y="246.61383"
       id="text2073-854"><tspan
         id="tspan2071-84"
         style="stroke-width:0.557"
         x="75.445107"
         y="246.61383">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.473396"
       y="252.12349"
       id="text2073-21"><tspan
         id="tspan2071-57"
         style="stroke-width:0.557"
         x="75.473396"
         y="252.12349">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.194672"
       y="257.38272"
       id="text2073-33"><tspan
         id="tspan2071-66"
         style="stroke-width:0.557"
         x="75.194672"
         y="257.38272">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.445107"
       y="263.17108"
       id="text2073-315"><tspan
         id="tspan2071-26"
         style="stroke-width:0.557"
         x="75.445107"
         y="263.17108">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.194672"
       y="268.37372"
       id="text2073-61"><tspan
         id="tspan2071-56"
         style="stroke-width:0.557"
         x="75.194672"
         y="268.37372">observacion</tspan></text>
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 133.5685,1491.515 v 210.8976"
       id="path13387"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 133.5685,1491.515 h 1.17166 v 210.8976 h -1.17166 z"
       id="path13389"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 841.24724,2601.0709 h 2.34331 v 51.5527 h -2.34331 z"
       id="path13391"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1129.474,2360.8819 h 2.3433 v 25.7764 h -2.3433 z"
       id="path13393"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1418.8724,2049.222 v 130.0536"
       id="path13395"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1418.8724,2049.222 h 1.1717 v 130.0536 h -1.1717 z"
       id="path13397"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 224.95748,561.22205 v 85.53071"
       id="path13399"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 224.95748,561.22205 h 1.17165 v 85.53071 h -1.17165 z"
       id="path13401"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 272.99528,2463.9874 h 2.3433 v 188.6362 h -2.3433 z"
       id="path13403"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 352.66772,2360.8819 h 2.3433 v 25.7764 h -2.3433 z"
       id="path13405"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 419.45197,2360.8819 h 2.34331 v 64.4409 h -2.34331 z"
       id="path13407"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 697.13386,2463.9874 h 2.34331 v 188.6362 h -2.34331 z"
       id="path13409"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 986.53228,561.22205 v 31.63464"
       id="path13411"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 986.53228,561.22205 h 1.17166 v 31.63464 h -1.17166 z"
       id="path13413"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1273.5874,2360.8819 h 2.3433 v 25.7764 h -2.3433 z"
       id="path13415"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1537.2094,2049.222 v 130.0536"
       id="path13417"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1537.2094,2049.222 h 1.1717 v 130.0536 h -1.1717 z"
       id="path13419"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 486.23622,2386.6583 h 2.34331 v 38.6645 h -2.34331 z"
       id="path13421"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,0 H 1656.7181"
       id="path13423"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,0 H 1656.7181 V 1.1716535 H 1.1716535 Z"
       id="path13425"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,209.72598 h 1656.7181 v 2.34331 H 0 Z"
       id="path13427"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 555.36378,249.5622 H 1656.7181"
       id="path13429"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 555.36378,249.5622 H 1656.7181 v 1.17166 H 555.36378 Z"
       id="path13431"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,305.80157 H 1656.7181"
       id="path13433"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,305.80157 H 1656.7181 v 1.17166 H 1.1716535 Z"
       id="path13435"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,350.32441 H 1656.7181"
       id="path13437"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,350.32441 H 1656.7181 v 1.17165 H 1.1716535 Z"
       id="path13439"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,394.84724 H 1656.7181"
       id="path13441"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,394.84724 H 1656.7181 v 1.17166 H 1.1716535 Z"
       id="path13443"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,439.37008 H 1656.7181"
       id="path13445"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,439.37008 H 1656.7181 v 1.17165 H 1.1716535 Z"
       id="path13447"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,483.89291 H 1656.7181"
       id="path13449"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,483.89291 H 1656.7181 v 1.17166 H 1.1716535 Z"
       id="path13451"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,528.41575 H 1656.7181"
       id="path13453"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,528.41575 H 1656.7181 v 1.17165 H 1.1716535 Z"
       id="path13455"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,560.05039 H 1656.7181"
       id="path13457"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,560.05039 H 1656.7181 v 1.17166 H 1.1716535 Z"
       id="path13459"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,591.68504 H 1656.7181"
       id="path13461"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,591.68504 H 1656.7181 v 1.17165 H 1.1716535 Z"
       id="path13463"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,618.63307 H 1656.7181"
       id="path13465"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,618.63307 H 1656.7181 v 1.17165 H 1.1716535 Z"
       id="path13467"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,645.5811 H 1656.7181"
       id="path13469"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,645.5811 H 1656.7181 v 1.17166 H 1.1716535 Z"
       id="path13471"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 355.01102,665.49921 H 555.36378"
       id="path13473"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 355.01102,665.49921 h 200.35276 v 1.17166 H 355.01102 Z"
       id="path13475"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,685.41732 H 1656.7181"
       id="path13477"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,685.41732 H 1656.7181 v 1.17166 H 1.1716535 Z"
       id="path13479"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,728.7685 H 1656.7181"
       id="path13481"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,728.7685 H 1656.7181 v 1.17166 H 1.1716535 Z"
       id="path13483"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,772.11969 H 1656.7181"
       id="path13485"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,772.11969 H 1656.7181 v 1.17165 H 134.74016 Z"
       id="path13487"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,815.47087 H 1656.7181"
       id="path13489"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,815.47087 H 1656.7181 v 1.17165 H 134.74016 Z"
       id="path13491"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,858.82205 H 1656.7181"
       id="path13493"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,858.82205 H 1656.7181 v 1.17165 H 134.74016 Z"
       id="path13495"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,902.17323 H 1656.7181"
       id="path13497"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,902.17323 H 1656.7181 v 1.17165 H 1.1716535 Z"
       id="path13499"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 355.01102,945.52441 H 1656.7181"
       id="path13501"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 355.01102,945.52441 H 1656.7181 v 1.17165 H 355.01102 Z"
       id="path13503"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 355.01102,988.87559 H 1656.7181"
       id="path13505"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 355.01102,988.87559 H 1656.7181 v 1.17165 H 355.01102 Z"
       id="path13507"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1032.2268 H 1656.7181"
       id="path13509"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1032.2268 H 1656.7181 v 1.1716 H 1.1716535 Z"
       id="path13511"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1075.578 H 1656.7181"
       id="path13513"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1075.578 H 1656.7181 v 1.1716 H 1.1716535 Z"
       id="path13515"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1118.9291 H 1656.7181"
       id="path13517"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1118.9291 H 1656.7181 v 1.1717 H 134.74016 Z"
       id="path13519"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1186.885 H 1656.7181"
       id="path13521"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1186.885 H 1656.7181 v 1.1717 H 134.74016 Z"
       id="path13523"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1230.2362 H 1656.7181"
       id="path13525"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1230.2362 H 1656.7181 v 1.1717 H 1.1716535 Z"
       id="path13527"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1273.5874 H 1656.7181"
       id="path13529"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1273.5874 H 1656.7181 v 1.1717 H 1.1716535 Z"
       id="path13531"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1316.9386 H 1656.7181"
       id="path13533"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1316.9386 H 1656.7181 v 1.1716 H 134.74016 Z"
       id="path13535"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1360.2898 H 1656.7181"
       id="path13537"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1360.2898 H 1656.7181 v 1.1716 H 134.74016 Z"
       id="path13539"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1403.6409 H 1656.7181"
       id="path13541"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1403.6409 H 1656.7181 v 1.1717 H 134.74016 Z"
       id="path13543"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1446.9921 H 1656.7181"
       id="path13545"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1446.9921 H 1656.7181 v 1.1717 H 1.1716535 Z"
       id="path13547"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1490.3433 H 1656.7181"
       id="path13549"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1490.3433 H 1656.7181 v 1.1717 H 1.1716535 Z"
       id="path13551"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1525.4929 H 1656.7181"
       id="path13553"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1525.4929 H 1656.7181 v 1.1717 H 134.74016 Z"
       id="path13555"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1560.6425 H 1656.7181"
       id="path13557"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1560.6425 H 1656.7181 v 1.1717 H 134.74016 Z"
       id="path13559"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1595.7921 H 1656.7181"
       id="path13561"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1595.7921 H 1656.7181 v 1.1717 H 1.1716535 Z"
       id="path13563"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1630.9417 H 1656.7181"
       id="path13565"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1630.9417 H 1656.7181 v 1.1717 H 134.74016 Z"
       id="path13567"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1666.0913 H 1656.7181"
       id="path13569"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1666.0913 H 1656.7181 v 1.1717 H 134.74016 Z"
       id="path13571"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1701.2409 H 1656.7181"
       id="path13573"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1701.2409 H 1656.7181 v 1.1717 H 1.1716535 Z"
       id="path13575"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1744.5921 H 1656.7181"
       id="path13577"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1744.5921 H 1656.7181 v 1.1717 H 1.1716535 Z"
       id="path13579"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1787.9433 H 1656.7181"
       id="path13581"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1787.9433 H 1656.7181 v 1.1717 H 1.1716535 Z"
       id="path13583"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1831.2945 H 1656.7181"
       id="path13585"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1831.2945 H 1656.7181 v 1.1716 H 1.1716535 Z"
       id="path13587"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1874.6457 H 1656.7181"
       id="path13589"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1874.6457 H 1656.7181 v 1.1716 H 1.1716535 Z"
       id="path13591"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1917.9969 H 1656.7181"
       id="path13593"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1917.9969 H 1656.7181 v 1.1716 H 1.1716535 Z"
       id="path13595"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1961.348 H 1656.7181"
       id="path13597"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1961.348 H 1656.7181 v 1.1717 H 1.1716535 Z"
       id="path13599"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2004.6992 H 1656.7181"
       id="path13601"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2004.6992 H 1656.7181 v 1.1717 H 1.1716535 Z"
       id="path13603"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2048.0504 H 1656.7181"
       id="path13605"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2048.0504 H 1656.7181 v 1.1716 H 1.1716535 Z"
       id="path13607"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2091.4016 H 1656.7181"
       id="path13609"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2091.4016 H 1656.7181 v 1.1716 H 1.1716535 Z"
       id="path13611"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2134.7528 H 1656.7181"
       id="path13613"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2134.7528 H 1656.7181 v 1.1716 H 1.1716535 Z"
       id="path13615"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2178.1039 H 1656.7181"
       id="path13617"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2178.1039 H 1656.7181 v 1.1717 H 1.1716535 Z"
       id="path13619"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2217.9402 h 1656.7181 v 2.3433 H 0 Z"
       id="path13621"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2241.3732 h 1656.7181 v 2.3433 H 0 Z"
       id="path13623"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2335.1055 h 1656.7181 v 2.3433 H 0 Z"
       id="path13625"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2358.5386 h 1656.7181 v 2.3433 H 0 Z"
       id="path13627"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2384.315 h 1656.7181 v 2.3433 H 0 Z"
       id="path13629"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2422.9795 h 1656.7181 v 2.3433 H 0 Z"
       id="path13631"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2461.6441 h 1656.7181 v 2.3433 H 0 Z"
       id="path13633"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2495.622 h 1656.7181 v 2.3434 H 0 Z"
       id="path13635"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2521.3984 h 275.33858 v 2.3433 H 0 Z"
       id="path13637"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2547.1748 h 275.33858 v 2.3433 H 0 Z"
       id="path13639"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2572.9512 h 275.33858 v 2.3433 H 0 Z"
       id="path13641"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 699.47717,2598.7276 h 957.24093 v 2.3433 H 699.47717 Z"
       id="path13643"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 699.47717,2624.5039 h 144.11338 v 2.3433 H 699.47717 Z"
       id="path13645"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2650.2803 h 1656.7181 v 2.3433 H 0 Z"
       id="path13647"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2861.178 H 1656.7181"
       id="path13649"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2861.178 H 1656.7181 v 1.1716 H 1.1716535 Z"
       id="path13651"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="M -1.1716535,-1.1716535 H 1657.8898 V 2.3433071 H -1.1716535 Z"
       id="path13653"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="M -1.1716535,2860.0063 H 1657.8898 v 3.515 H -1.1716535 Z"
       id="path13655"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-opacity:1"
       clip-path="url(#clipEmfPath2)"
       d="M -1.1716535,-1.1716535 H 2.3433071 V 2863.5213 h -3.5149606 z"
       id="path13657"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-opacity:1"
       clip-path="url(#clipEmfPath2)"
       d="m 1654.3748,-1.1716535 h 3.515 V 2863.5213 h -3.515 z"
       id="path13659"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" />
    <g
       id="g15703"
       style="stroke:#000000;stroke-opacity:1">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679" />
      <g
         id="g15698"
         style="stroke:#000000;stroke-opacity:1">
        <path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677" />
      </g>
    </g>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="97.91362"
       y="79.954216"
       id="text30644-3"><tspan
         id="tspan30642-1"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="97.91362"
         y="79.954216">X</tspan></text>
    <g
       id="g15703-5"
       style="stroke:#000000;stroke-opacity:1"
       transform="translate(83.164521,9.2156325)">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1" />
      <g
         id="g15698-7"
         style="stroke:#000000;stroke-opacity:1">
        <path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19" />
      </g>
    </g>
    <g
       id="g15703-5-1"
       style="stroke:#000000;stroke-opacity:1"
       transform="translate(83.164521,36.174921)">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4" />
      <g
         id="g15698-7-9"
         style="stroke:#000000;stroke-opacity:1">
        <path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8" />
      </g>
    </g>
    <g
       id="g15703-5-1-4"
       style="stroke:#000000;stroke-opacity:1"
       transform="translate(83.14213,41.638431)">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2" />
      <g
         id="g15698-7-9-3"
         style="stroke:#000000;stroke-opacity:1">
        <path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1" />
      </g>
    </g>
    <g
       id="g15703-0"
       style="stroke:#000000;stroke-opacity:1"
       transform="translate(23.71526,-0.07681331)">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-6" />
      <g
         id="g15698-5"
         style="stroke:#000000;stroke-opacity:1">
        <path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-1" />
      </g>
    </g>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="121.91724"
       y="79.685524"
       id="text30644-82"><tspan
         id="tspan30642-78"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="121.91724"
         y="79.685524">X</tspan></text>
    <path
       style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:0.306;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
       d="m 147.40002,77.337225 c 0,-0.30116 0,-0.562167 0,-0.562167 v 0 c 0,0 0,0.261007 0,0.562167 v 2.24866 c 0,0.311201 0,0.562166 0,0.562166 v 0 c 0,0 0,-0.250965 0,-0.562166 z"
       id="path13685" />
    <path
       style="fill:#ffffff;fill-opacity:1;fill-rule:evenodd;stroke:none;stroke-width:0.127223"
       d="m 3.9734788,6.1857043 c 0,-1.5645481 1.3358459,-2.8380181 2.9770273,-2.8380181 H 43.132828 c 1.650724,0 2.977028,1.27347 2.977028,2.8380181 V 17.53778 c 0,1.573649 -1.326304,2.83802 -2.977028,2.83802 H 6.9505061 c -1.6411814,0 -2.9770273,-1.264371 -2.9770273,-2.83802 z"
       id="path13753" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
       d="m 3.9734788,6.1857043 c 0,-1.5645481 1.3358459,-2.8380181 2.9770273,-2.8380181 H 43.132828 c 1.650724,0 2.977028,1.27347 2.977028,2.8380181 V 17.53778 c 0,1.573649 -1.326304,2.83802 -2.977028,2.83802 H 6.9505061 c -1.6411814,0 -2.9770273,-1.264371 -2.9770273,-2.83802 z"
       id="path13755" />
    <g
       id="g13759"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)">
      <rect
         style="clip-rule:nonzero;display:inline;overflow:visible;visibility:visible;color-interpolation:sRGB;color-interpolation-filters:linearRGB;fill:#ffffff;stroke:none;stroke-dasharray:none;marker:none;enable-background:accumulate"
         width="88.987335"
         height="11.422485"
         x="0"
         y="-11.259552"
         transform="translate(147.61353,101.2038)"
         id="rect13757" />
    </g>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:400;font-size:2.23436px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.127223"
       x="18.783827"
       y="12.875729"
       id="text13765"
       transform="scale(1.0241975,0.97637415)"><tspan
         x="18.783827"
         y="12.875729"
         id="tspan13763"
         style="stroke-width:0.127223"><tspan
           dx="0"
           dy="0"
           style="font-style:normal;font-variant:normal;font-weight:400;font-size:2.23436px;font-family:Calibri;fill:#000000;stroke-width:0.127223"
           id="tspan13761">SELLO ONAC</tspan></tspan></text>
    <g
       id="g15703-5-1-4-4"
       style="stroke:#000000;stroke-opacity:1"
       transform="translate(83.209304,46.810852)">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-9" />
      <g
         id="g15698-7-9-3-1"
         style="stroke:#000000;stroke-opacity:1">
        <path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-1" />
      </g>
    </g>
    <g
       id="g15703-5-1-4-7"
       style="stroke:#000000;stroke-opacity:1"
       transform="translate(83.14213,52.050448)">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-5" />
      <g
         id="g15698-7-9-3-9"
         style="stroke:#000000;stroke-opacity:1">
        <path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-2" />
      </g>
    </g>
    <g
       id="g15703-5-1-4-43"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0068089,0,0,0.76531115,82.444503,74.880612)">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-50" />
      <g
         id="g15698-7-9-3-3"
         style="stroke:#000000;stroke-opacity:1">
        <path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-19" />
      </g>
    </g>
    <g
       id="g15703-5-1-4-76"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,82.49733,76.038519)">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90" />
      <g
         id="g15698-7-9-3-10"
         style="stroke:#000000;stroke-opacity:1">
        <path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22" />
      </g>
    </g>
    <g
       id="g15703-5-1-4-76-4"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,82.474943,87.446955)">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-0" />
      <g
         id="g15698-7-9-3-10-8"
         style="stroke:#000000;stroke-opacity:1">
        <path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-3" />
      </g>
    </g>
    <g
       id="g15703-5-1-4-76-3"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,82.474943,89.865231)">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-5" />
      <g
         id="g15698-7-9-3-10-58"
         style="stroke:#000000;stroke-opacity:1">
        <path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-4" />
      </g>
    </g>
    <g
       id="g15703-5-1-4-76-40"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,82.519725,92.8209)">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-06" />
      <g
         id="g15698-7-9-3-10-56"
         style="stroke:#000000;stroke-opacity:1">
        <path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-8" />
      </g>
    </g>
    <g
       id="g15703-5-1-4-76-2"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,82.564508,95.373523)">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-15" />
      <g
         id="g15698-7-9-3-10-88"
         style="stroke:#000000;stroke-opacity:1">
        <path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-88" />
      </g>
    </g>
    <g
       id="g15703-5-1-4-76-49"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,-28.900055,241.94786)">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-55" />
      <g
         id="g15698-7-9-3-10-82"
         style="stroke:#000000;stroke-opacity:1">
        <path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-20" />
      </g>
    </g>
    <g
       id="g15703-5-1-4-76-75"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,-10.85256,241.94786)">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-8" />
      <g
         id="g15698-7-9-3-10-4"
         style="stroke:#000000;stroke-opacity:1">
        <path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-6" />
      </g>
    </g>
    <g
       id="g15703-5-1-4-76-6"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,-81.833407,262.90624)">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-81" />
      <g
         id="g15698-7-9-3-10-588"
         style="stroke:#000000;stroke-opacity:1">
        <path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-31" />
      </g>
    </g>
    <g
       id="g15703-5-1-4-76-9"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,-81.788627,259.72666)">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-4" />
      <g
         id="g15698-7-9-3-10-81"
         style="stroke:#000000;stroke-opacity:1">
        <path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-5" />
      </g>
    </g>
    <g
       id="g15703-5-1-4-76-1"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,-81.833407,256.63664)">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-9" />
      <g
         id="g15698-7-9-3-10-6"
         style="stroke:#000000;stroke-opacity:1">
        <path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-61" />
      </g>
    </g>
    <g
       id="g15703-5-1-4-76-0"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,-81.833413,253.50185)">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-78" />
      <g
         id="g15698-7-9-3-10-86"
         style="stroke:#000000;stroke-opacity:1">
        <path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-7" />
      </g>
    </g>
    <g
       id="g15703-5-1-4-76-34"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,-81.833407,250.25509)">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-98" />
      <g
         id="g15698-7-9-3-10-49"
         style="stroke:#000000;stroke-opacity:1">
        <path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-56" />
      </g>
    </g>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:700;font-size:1.78573px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.117097"
       transform="scale(0.94268024,1.0608051)"
       x="58.391376"
       y="237.87152"
       id="text11753-8"><tspan
         x="58.391376"
         y="237.87152"
         id="tspan11751-3"
         style="stroke-width:0.117097">REGULAR</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:2.64583px;font-family:Arial;-inkscape-font-specification:Arial;opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="38.506187"
       y="29.322969"
       id="text30514"><tspan
         id="tspan30512"
         style="fill:#000000;stroke-width:0.306"
         x="38.506187"
         y="29.322969">FECHA AQUI</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:2.64583px;font-family:Arial;-inkscape-font-specification:Arial;opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="20.499691"
       y="34.865135"
       id="text30518"><tspan
         id="tspan30516"
         style="stroke-width:0.306"
         x="20.499691"
         y="34.865135">Propietario o empresa aqui</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:2.64583px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="20.485865"
       y="41.447346"
       id="text30518-4"><tspan
         id="tspan30516-4"
         style="stroke-width:0.306"
         x="20.485865"
         y="41.447346">NIT mpresa aqui</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:2.64583px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="20.488251"
       y="47.470985"
       id="text30518-6"><tspan
         id="tspan30516-0"
         style="stroke-width:0.306"
         x="20.488251"
         y="47.470985">Usuario empresa aqui</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:2.64583px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="20.467396"
       y="52.721764"
       id="text30518-1"><tspan
         id="tspan30516-5"
         style="stroke-width:0.306"
         x="20.467396"
         y="52.721764">PDireccion empresa aqui</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:2.64583px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="20.629684"
       y="58.179844"
       id="text30518-7"><tspan
         id="tspan30516-06"
         style="stroke-width:0.306"
         x="20.629684"
         y="58.179844">Telefono o empresa aqui</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:2.64583px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="20.517611"
       y="63.585449"
       id="text30518-18"><tspan
         id="tspan30516-7"
         style="stroke-width:0.306"
         x="20.517611"
         y="63.585449">Contacto o empresa aqui</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:2.64583px;font-family:Arial;-inkscape-font-specification:Arial;opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="165.06966"
       y="52.754219"
       id="text30619"><tspan
         id="tspan30617"
         style="stroke-width:0.306"
         x="165.06966"
         y="52.754219">9999</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:2.64583px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="161.35431"
       y="58.095707"
       id="text30518-5"><tspan
         id="tspan30516-46"
         style="stroke-width:0.306"
         x="161.35431"
         y="58.095707">Fabricante empresa aqui</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:2.64583px;font-family:Arial;-inkscape-font-specification:Arial;opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="161.5766"
       y="63.770805"
       id="text30640"><tspan
         id="tspan30638"
         style="stroke-width:0.306"
         x="161.5766"
         y="63.770805">999999999999</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="31.437572"
       y="72.637817"
       id="text30644"><tspan
         id="tspan30642"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="31.437572"
         y="72.637817">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="48.831593"
       y="88.910789"
       id="text30644-35"><tspan
         id="tspan30642-37"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="48.831593"
         y="88.910789">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.192574"
       y="144.97894"
       id="text30644-75"><tspan
         id="tspan30642-43"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.192574"
         y="144.97894">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.146431"
       y="197.28534"
       id="text30644-85-1"><tspan
         id="tspan30642-905-0"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.146431"
         y="197.28534">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="66.834305"
       y="197.28534"
       id="text30644-85-10"><tspan
         id="tspan30642-905-1"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="66.834305"
         y="197.28534">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.368988"
       y="201.40536"
       id="text30644-85-9"><tspan
         id="tspan30642-905-9"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.368988"
         y="201.40536">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.325562"
       y="201.40536"
       id="text30644-85-3"><tspan
         id="tspan30642-905-94"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.325562"
         y="201.40536">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="66.744743"
       y="201.40536"
       id="text30644-85-90"><tspan
         id="tspan30642-905-3"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="66.744743"
         y="201.40536">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.189857"
       y="205.88365"
       id="text30644-85-8"><tspan
         id="tspan30642-905-6"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.189857"
         y="205.88365">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.235996"
       y="206.06277"
       id="text30644-85-7"><tspan
         id="tspan30642-905-7"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.235996"
         y="206.06277">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.192574"
       y="205.97322"
       id="text30644-85-37"><tspan
         id="tspan30642-905-18"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.192574"
         y="205.97322">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.279423"
       y="210.09325"
       id="text30644-85-89"><tspan
         id="tspan30642-905-67"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.279423"
         y="210.09325">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.235996"
       y="210.1828"
       id="text30644-85-87"><tspan
         id="tspan30642-905-37"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.235996"
         y="210.1828">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.192574"
       y="210.09325"
       id="text30644-85-0"><tspan
         id="tspan30642-905-8"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.192574"
         y="210.09325">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="48.831593"
       y="220.84113"
       id="text30644-85-89-1"><tspan
         id="tspan30642-905-67-3"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="48.831593"
         y="220.84113">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="48.921158"
       y="225.76724"
       id="text30644-85-89-10"><tspan
         id="tspan30642-905-67-6"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="48.921158"
         y="225.76724">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="48.652462"
       y="236.8734"
       id="text30644-85-89-2"><tspan
         id="tspan30642-905-67-74"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="48.652462"
         y="236.8734">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="48.921158"
       y="242.42647"
       id="text30644-85-89-83"><tspan
         id="tspan30642-905-67-41"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="48.921158"
         y="242.42647">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="48.831593"
       y="258.54831"
       id="text30644-85-89-08"><tspan
         id="tspan30642-905-67-61"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="48.831593"
         y="258.54831">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.100292"
       y="263.83267"
       id="text30644-85-89-34"><tspan
         id="tspan30642-905-67-33"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.100292"
         y="263.83267">X</tspan></text>
    <g
       clip-path="url(#clipEmfPath2)"
       id="g11341"
       transform="matrix(0.13030134,0,0,0.12421712,-2.3209546,0.08984492)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(169.88976,567.08032)"
         x="0"
         y="12.730408"
         id="text10775"><tspan
           x="0"
           y="12.730408"
           id="tspan10773"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan10771">PLANTA</tspan></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(169.88976,567.08032)"
         x="131.2252"
         y="12.730408"
         id="text10781"><tspan
           x="131.2252"
           y="12.730408"
           id="tspan10779"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan10777">IN-SITU</tspan></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(169.88976,567.08032)"
         x="631.52124"
         y="12.000221"
         id="text10787"><tspan
           x="631.52124"
           y="12.000221"
           id="tspan10785"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan10783">1 VEZ</tspan></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(169.88976,567.08032)"
         x="919.74805"
         y="12.000221"
         id="text10793"><tspan
           x="919.74805"
           y="12.000221"
           id="tspan10791"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan10789">2 VEZ</tspan></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         x="160.35777"
         y="610.17706"
         id="text10799"><tspan
           x="160.35777"
           y="610.17706"
           id="tspan10797"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan10795">VERTICAL</tspan></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(169.88976,567.08032)"
         x="1152.9071"
         y="43.09676"
         id="text10805"><tspan
           x="1152.9071"
           y="43.09676"
           id="tspan10803"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan10801">ENTERRADO</tspan></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(169.88976,567.08032)"
         x="213.24095"
         y="111.59011"
         id="text10811"><tspan
           x="213.24095"
           y="111.59011"
           id="tspan10809"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;font-family:Calibri;fill:#000000"
             id="tspan10807">SI</tspan></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(169.88976,567.08032)"
         x="276.51022"
         y="111.59011"
         id="text10817"><tspan
           x="276.51022"
           y="111.59011"
           id="tspan10815"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;font-family:Calibri;fill:#000000"
             id="tspan10813">NO</tspan></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         x="527.08533"
         y="678.67041"
         id="text10823"><tspan
           x="527.08533"
           y="678.67041"
           id="tspan10821"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;font-family:Calibri;fill:#000000"
             id="tspan10819">N/A</tspan></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(169.88976,567.08032)"
         x="212.06929"
         y="143.22542"
         id="text10829"><tspan
           x="0"
           y="0"
           id="tspan10827"><tspan
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Calibri;fill:#f2f2f2"
             id="tspan10825" /></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(169.88976,567.08032)"
         x="1418.8724"
         y="143.83435"
         id="text10853"><tspan
           x="0"
           y="0"
           id="tspan10851"><tspan
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Calibri;fill:#000000"
             id="tspan10849" /></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:16.375px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         x="374.77036"
         y="1474.7041"
         id="text11339"><tspan
           x="374.77036"
           y="1474.7041"
           id="tspan11337"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:16.375px;font-family:Arial;fill:#000000"
             id="tspan11335">BUENO</tspan></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:16.375px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         x="377.42584"
         y="1732.7538"
         id="text11339-4"><tspan
           x="377.42584"
           y="1732.7538"
           id="tspan11337-3"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:16.375px;font-family:Arial;fill:#000000"
             id="tspan11335-8">BUENO</tspan></tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5129px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.997177"
         transform="scale(0.99562284,1.0043964)"
         x="523.21808"
         y="1468.2401"
         id="text11565-6"><tspan
           x="523.21808"
           y="1468.2401"
           id="tspan11563-2"
           style="stroke-width:0.997177"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5129px;font-family:Arial;fill:#000000;stroke-width:0.997177"
             id="tspan11561-9">N/A</tspan></tspan></text>
    </g>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.09425"
       y="156.89119"
       id="text30644-85-89-235-2"><tspan
         id="tspan30642-905-67-42-80"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.09425"
         y="156.89119">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.18382"
       y="161.90688"
       id="text30644-85-89-235-65"><tspan
         id="tspan30642-905-67-42-4"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.18382"
         y="161.90688">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.27339"
       y="167.54951"
       id="text30644-85-89-235-3"><tspan
         id="tspan30642-905-67-42-46"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.27339"
         y="167.54951">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.18382"
       y="172.83389"
       id="text30644-85-89-235-01"><tspan
         id="tspan30642-905-67-42-00"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.18382"
         y="172.83389">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.36296"
       y="177.93915"
       id="text30644-85-89-235-5"><tspan
         id="tspan30642-905-67-42-02"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.36296"
         y="177.93915">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.18382"
       y="151.33812"
       id="text30644-85-89-235-22"><tspan
         id="tspan30642-905-67-42-20"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.18382"
         y="151.33812">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.59938"
       y="151.15898"
       id="text30644-85-89-235-27"><tspan
         id="tspan30642-905-67-42-7"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.59938"
         y="151.15898">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.50983"
       y="143.90416"
       id="text30644-85-89-235-7"><tspan
         id="tspan30642-905-67-42-21"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.50983"
         y="143.90416">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.27339"
       y="144.26242"
       id="text30644-85-89-235-34"><tspan
         id="tspan30642-905-67-42-09"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.27339"
         y="144.26242">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.09425"
       y="137.45543"
       id="text30644-85-89-235-99"><tspan
         id="tspan30642-905-67-42-6"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.09425"
         y="137.45543">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.42026"
       y="137.63455"
       id="text30644-85-89-235-04"><tspan
         id="tspan30642-905-67-42-42"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.42026"
         y="137.63455">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.50983"
       y="131.90236"
       id="text30644-85-89-235-49"><tspan
         id="tspan30642-905-67-42-63"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.50983"
         y="131.90236">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.77852"
       y="126.61797"
       id="text30644-85-89-235-08"><tspan
         id="tspan30642-905-67-42-88"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.77852"
         y="126.61797">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.77852"
       y="121.60229"
       id="text30644-85-89-235-32"><tspan
         id="tspan30642-905-67-42-70"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.77852"
         y="121.60229">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.77852"
       y="115.60139"
       id="text30644-85-89-235-03"><tspan
         id="tspan30642-905-67-42-3"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.77852"
         y="115.60139">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.68895"
       y="110.49614"
       id="text30644-85-89-235-74"><tspan
         id="tspan30642-905-67-42-06"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.68895"
         y="110.49614">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.77852"
       y="105.03263"
       id="text30644-85-89-235-95"><tspan
         id="tspan30642-905-67-42-37"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.77852"
         y="105.03263">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.7785"
       y="99.882591"
       id="text30644-85-89-235-59"><tspan
         id="tspan30642-905-67-42-40"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.7785"
         y="99.882591">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="192.00243"
       y="94.329521"
       id="text30644-85-89-235-93"><tspan
         id="tspan30642-905-67-42-99"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="192.00243"
         y="94.329521">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.8233"
       y="88.821228"
       id="text30644-85-89-235-93-1"><tspan
         id="tspan30642-905-67-42-99-2"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.8233"
         y="88.821228">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.0047"
       y="88.821228"
       id="text30644-85-89-235-30"><tspan
         id="tspan30642-905-67-42-39"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.0047"
         y="88.821228">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.18382"
       y="94.105606"
       id="text30644-85-89-235-43"><tspan
         id="tspan30642-905-67-42-91"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.18382"
         y="94.105606">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.09425"
       y="99.569122"
       id="text30644-85-89-235-29"><tspan
         id="tspan30642-905-67-42-61"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.09425"
         y="99.569122">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.18382"
       y="105.21176"
       id="text30644-85-89-235-1"><tspan
         id="tspan30642-905-67-42-465"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.18382"
         y="105.21176">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.27339"
       y="110.67527"
       id="text30644-85-89-235-12"><tspan
         id="tspan30642-905-67-42-05"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.27339"
         y="110.67527">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.09425"
       y="115.87009"
       id="text30644-85-89-235-58"><tspan
         id="tspan30642-905-67-42-87"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.09425"
         y="115.87009">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.09425"
       y="121.3336"
       id="text30644-85-89-235-07"><tspan
         id="tspan30642-905-67-42-34"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.09425"
         y="121.3336">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.0047"
       y="126.61797"
       id="text30644-85-89-235-00"><tspan
         id="tspan30642-905-67-42-82"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.0047"
         y="126.61797">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.0047"
       y="132.35017"
       id="text30644-85-89-235-13"><tspan
         id="tspan30642-905-67-42-47"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.0047"
         y="132.35017">X</tspan></text>
    <path
       d="m 180.72535,87.827024 c 0.007,0.0084 0.0237,0.02963 0.0517,0.09083 0.0135,0.02941 0.0236,0.05411 0.0429,0.09959 0.008,0.01958 0.0204,0.04798 0.0338,0.07692 0.0332,0.07572 0.0744,0.181422 0.13027,0.309923 0.0421,0.09676 0.0978,0.216747 0.17203,0.33551 0.0156,0.02987 0.0357,0.06081 0.0619,0.09034 0.0348,0.0393 0.0794,0.07499 0.13409,0.100462 0.0539,0.0251 0.11017,0.03678 0.16463,0.03747 0.0527,6.69e-4 0.10011,-0.0089 0.14023,-0.02258 0.0394,-0.01343 0.0737,-0.03142 0.10259,-0.05034 0.0287,-0.01879 0.054,-0.03981 0.076,-0.06151 0.0336,-0.03311 0.0637,-0.07178 0.0879,-0.114564 0.0485,-0.06894 0.0892,-0.138894 0.12118,-0.193135 0.0387,-0.0656 0.0668,-0.111608 0.0974,-0.151774 0.003,-0.0044 0.007,-0.0089 0.01,-0.01341 0.44577,-0.647021 0.92583,-1.15605 1.46199,-1.521096 0.1375,-0.09427 0.25309,-0.162413 0.32322,-0.202331 a 0.3405575,0.3405575 90 0 0 -0.33698,-0.59192 c -0.0805,0.04585 -0.2134,0.124179 -0.37047,0.23186 -0.62067,0.422579 -1.15573,0.997354 -1.63425,1.690697 -0.056,0.07434 -0.10104,0.150506 -0.13717,0.211717 -0.0399,0.06759 -0.068,0.115312 -0.0997,0.158547 -0.013,0.01773 -0.0242,0.03667 -0.0335,0.05656 0.009,-0.01884 0.0199,-0.03387 0.0328,-0.04658 0.007,-0.0069 0.0163,-0.0148 0.0284,-0.02272 0.0121,-0.0079 0.0291,-0.01723 0.0512,-0.02477 0.0226,-0.0077 0.0525,-0.01417 0.088,-0.01372 0.037,4.71e-4 0.0764,0.0085 0.11423,0.02613 0.0384,0.01786 0.0675,0.04198 0.0883,0.06542 0.0206,0.02324 0.0319,0.04459 0.0377,0.05779 l -0.0252,-0.04697 c -0.0503,-0.0785 -0.0924,-0.166374 -0.13168,-0.256678 -0.0479,-0.110072 -0.0914,-0.221411 -0.13383,-0.317893 -0.0112,-0.02437 -0.0198,-0.04459 -0.0278,-0.0633 -0.0163,-0.03831 -0.032,-0.07648 -0.0508,-0.117459 -0.0501,-0.109349 -0.0967,-0.180536 -0.14272,-0.237111 a 0.3405575,0.3405575 90 0 0 -0.52816,0.430086 z"
       id="path-1"
       style="opacity:1;fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.293169;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 180.74705,114.84933 c 0.007,0.008 0.0237,0.0296 0.0517,0.0908 0.0135,0.0294 0.0236,0.0541 0.0429,0.0996 0.008,0.0196 0.0204,0.048 0.0338,0.0769 0.0332,0.0757 0.0744,0.18142 0.13027,0.30992 0.0421,0.0968 0.0978,0.21674 0.17202,0.33551 0.0156,0.0299 0.0357,0.0608 0.0619,0.0903 0.0348,0.0393 0.0794,0.075 0.13412,0.10048 0.0539,0.0251 0.11019,0.0368 0.16466,0.0375 0.0527,6.6e-4 0.10012,-0.009 0.14023,-0.0226 0.0394,-0.0134 0.0737,-0.0314 0.10257,-0.0503 0.0287,-0.0188 0.054,-0.0398 0.076,-0.0615 0.0336,-0.0331 0.0636,-0.0718 0.0879,-0.11454 0.0485,-0.0689 0.0892,-0.13889 0.12118,-0.19313 0.0387,-0.0656 0.0667,-0.1116 0.0974,-0.15177 0.003,-0.004 0.007,-0.009 0.01,-0.0134 0.44577,-0.64702 0.92582,-1.15605 1.46199,-1.52109 0.1375,-0.0943 0.25309,-0.16241 0.32322,-0.20233 a 0.3405575,0.3405575 90 0 0 -0.33698,-0.59192 c -0.0805,0.0459 -0.2134,0.12418 -0.37046,0.23185 -0.62069,0.42259 -1.15574,0.99736 -1.63426,1.6907 -0.0559,0.0743 -0.10103,0.1505 -0.13717,0.21171 -0.0399,0.0676 -0.068,0.1153 -0.0996,0.15854 -0.013,0.0177 -0.0242,0.0367 -0.0335,0.0566 0.009,-0.0188 0.0199,-0.0338 0.0328,-0.0465 0.007,-0.007 0.0163,-0.0148 0.0283,-0.0227 0.0121,-0.008 0.0291,-0.0172 0.0512,-0.0248 0.0226,-0.008 0.0524,-0.0142 0.088,-0.0137 0.037,4.6e-4 0.0764,0.008 0.11426,0.0261 0.0384,0.0179 0.0676,0.042 0.0883,0.0654 0.0206,0.0233 0.0319,0.0446 0.0377,0.0578 l -0.0252,-0.047 c -0.0504,-0.0785 -0.0924,-0.16638 -0.13168,-0.25669 -0.0479,-0.11007 -0.0914,-0.22141 -0.13383,-0.31789 -0.0112,-0.0244 -0.0198,-0.0446 -0.0278,-0.0633 -0.0162,-0.0383 -0.032,-0.0765 -0.0508,-0.11746 -0.0501,-0.10935 -0.0967,-0.18053 -0.14272,-0.23711 a 0.3405575,0.3405575 90 0 0 -0.52816,0.43008 z"
       id="path-1-3"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.293169;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 180.74705,120.26807 c 0.007,0.008 0.0237,0.0296 0.0517,0.0908 0.0135,0.0294 0.0236,0.0541 0.0429,0.0996 0.008,0.0196 0.0204,0.048 0.0338,0.0769 0.0332,0.0757 0.0744,0.18142 0.13027,0.30992 0.0421,0.0968 0.0978,0.21674 0.17203,0.3355 0.0156,0.0299 0.0357,0.0608 0.0619,0.0903 0.0348,0.0393 0.0794,0.075 0.13412,0.10048 0.0539,0.0251 0.11019,0.0368 0.16466,0.0374 0.0527,6.6e-4 0.10012,-0.009 0.14023,-0.0226 0.0394,-0.0134 0.0737,-0.0314 0.10257,-0.0503 0.0287,-0.0188 0.054,-0.0398 0.076,-0.0615 0.0336,-0.0331 0.0636,-0.0718 0.0879,-0.11454 0.0485,-0.0689 0.0892,-0.13889 0.12118,-0.19313 0.0387,-0.0656 0.0667,-0.1116 0.0974,-0.15177 0.003,-0.004 0.007,-0.009 0.01,-0.0134 0.44577,-0.64702 0.92583,-1.15604 1.46199,-1.52108 0.13749,-0.0943 0.25311,-0.16243 0.32322,-0.20234 a 0.3405575,0.3405575 90 0 0 -0.33698,-0.59192 c -0.0805,0.0458 -0.21342,0.12419 -0.37048,0.23187 -0.62066,0.42256 -1.15572,0.99734 -1.63424,1.69068 -0.0559,0.0743 -0.10103,0.1505 -0.13717,0.21171 -0.0399,0.0676 -0.068,0.1153 -0.0996,0.15854 -0.013,0.0177 -0.0242,0.0367 -0.0335,0.0566 0.009,-0.0188 0.0199,-0.0338 0.0328,-0.0465 0.007,-0.007 0.0163,-0.0148 0.0283,-0.0227 0.0121,-0.008 0.0291,-0.0172 0.0512,-0.0248 0.0226,-0.008 0.0524,-0.0142 0.088,-0.0137 0.037,4.6e-4 0.0764,0.008 0.11426,0.0261 0.0384,0.0179 0.0676,0.042 0.0883,0.0654 0.0206,0.0233 0.0319,0.0446 0.0377,0.0578 l -0.0252,-0.047 c -0.0504,-0.0785 -0.0924,-0.16638 -0.13168,-0.25668 -0.0479,-0.11007 -0.0914,-0.22141 -0.13383,-0.31789 -0.0112,-0.0244 -0.0198,-0.0446 -0.0278,-0.0633 -0.0162,-0.0383 -0.032,-0.0765 -0.0508,-0.11746 -0.0501,-0.10935 -0.0967,-0.18053 -0.14272,-0.23711 a 0.3405575,0.3405575 90 0 0 -0.52816,0.43008 z"
       id="path-1-6"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.293169;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 180.74705,125.46288 c 0.007,0.008 0.0237,0.0296 0.0517,0.0908 0.0135,0.0294 0.0236,0.0541 0.0429,0.0996 0.008,0.0196 0.0204,0.048 0.0338,0.0769 0.0332,0.0757 0.0744,0.18141 0.13026,0.30991 0.0421,0.0968 0.0978,0.21675 0.17203,0.33551 0.0156,0.0299 0.0357,0.0608 0.0619,0.0903 0.0348,0.0393 0.0794,0.075 0.13412,0.10048 0.0539,0.0251 0.11019,0.0368 0.16466,0.0375 0.0527,6.6e-4 0.10012,-0.009 0.14023,-0.0226 0.0394,-0.0134 0.0737,-0.0314 0.10257,-0.0503 0.0287,-0.0188 0.054,-0.0398 0.076,-0.0615 0.0336,-0.0331 0.0636,-0.0718 0.0879,-0.11454 0.0485,-0.0689 0.0892,-0.13889 0.12118,-0.19313 0.0387,-0.0656 0.0667,-0.1116 0.0974,-0.15177 0.003,-0.004 0.007,-0.009 0.01,-0.0134 0.44577,-0.64702 0.92583,-1.15604 1.46199,-1.52108 0.13749,-0.0943 0.25311,-0.16243 0.32322,-0.20234 a 0.3405575,0.3405575 90 0 0 -0.33698,-0.59192 c -0.0805,0.0458 -0.21342,0.12419 -0.37048,0.23187 -0.62066,0.42256 -1.15572,0.99734 -1.63424,1.69068 -0.0559,0.0743 -0.10103,0.1505 -0.13717,0.21171 -0.0399,0.0676 -0.068,0.1153 -0.0996,0.15854 -0.013,0.0177 -0.0242,0.0367 -0.0335,0.0566 0.009,-0.0188 0.0199,-0.0338 0.0328,-0.0465 0.007,-0.007 0.0163,-0.0148 0.0283,-0.0227 0.0121,-0.008 0.0291,-0.0172 0.0512,-0.0248 0.0226,-0.008 0.0524,-0.0142 0.088,-0.0137 0.037,4.6e-4 0.0764,0.008 0.11426,0.0261 0.0384,0.0179 0.0676,0.042 0.0883,0.0654 0.0206,0.0233 0.0319,0.0446 0.0377,0.0578 l -0.0252,-0.047 c -0.0504,-0.0785 -0.0924,-0.16638 -0.13168,-0.25668 -0.0479,-0.11007 -0.0914,-0.22142 -0.13383,-0.3179 -0.0112,-0.0244 -0.0198,-0.0446 -0.0278,-0.0633 -0.0162,-0.0383 -0.032,-0.0765 -0.0508,-0.11745 -0.0501,-0.10935 -0.0967,-0.18053 -0.14272,-0.23711 a 0.3405575,0.3405575 90 0 0 -0.52816,0.43008 z"
       id="path-1-5"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.293169;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 180.70227,130.65769 c 0.007,0.008 0.0237,0.0296 0.0517,0.0908 0.0135,0.0294 0.0236,0.0541 0.0429,0.0996 0.008,0.0196 0.0204,0.048 0.0338,0.0769 0.0332,0.0757 0.0744,0.18142 0.13027,0.30992 0.0421,0.0968 0.0978,0.21674 0.17203,0.3355 0.0156,0.0299 0.0357,0.0608 0.0619,0.0903 0.0348,0.0393 0.0794,0.075 0.13412,0.10048 0.0539,0.0251 0.11019,0.0368 0.16466,0.0375 0.0527,6.6e-4 0.10012,-0.009 0.14023,-0.0226 0.0394,-0.0134 0.0737,-0.0314 0.10257,-0.0503 0.0287,-0.0188 0.054,-0.0398 0.076,-0.0615 0.0336,-0.0331 0.0636,-0.0718 0.0879,-0.11453 0.0485,-0.0689 0.0892,-0.13888 0.12119,-0.19312 0.0387,-0.0656 0.0668,-0.11162 0.0974,-0.1518 0.003,-0.004 0.007,-0.009 0.01,-0.0134 0.44577,-0.64703 0.92582,-1.15605 1.46199,-1.52109 0.13749,-0.0943 0.25311,-0.16243 0.32322,-0.20234 a 0.3405575,0.3405575 90 0 0 -0.33698,-0.59192 c -0.0805,0.0458 -0.21342,0.12419 -0.37048,0.23187 -0.62067,0.42257 -1.15572,0.99735 -1.63425,1.6907 -0.0559,0.0743 -0.10102,0.15048 -0.13715,0.21169 -0.0399,0.0676 -0.068,0.1153 -0.0997,0.15853 -0.013,0.0177 -0.0242,0.0367 -0.0335,0.0566 0.009,-0.0188 0.0199,-0.0338 0.0328,-0.0465 0.007,-0.007 0.0163,-0.0148 0.0283,-0.0227 0.0121,-0.008 0.0291,-0.0172 0.0512,-0.0248 0.0226,-0.008 0.0524,-0.0142 0.088,-0.0137 0.0371,4.6e-4 0.0764,0.008 0.11426,0.0261 0.0384,0.0179 0.0676,0.042 0.0883,0.0654 0.0206,0.0233 0.0319,0.0446 0.0377,0.0578 l -0.0252,-0.047 c -0.0504,-0.0785 -0.0924,-0.16638 -0.13168,-0.25668 -0.0479,-0.11007 -0.0914,-0.22141 -0.13383,-0.31789 -0.0112,-0.0244 -0.0198,-0.0446 -0.0278,-0.0633 -0.0163,-0.0383 -0.032,-0.0765 -0.0508,-0.11746 -0.0501,-0.10935 -0.0967,-0.18053 -0.14272,-0.23711 a 0.3405575,0.3405575 90 0 0 -0.52816,0.43008 z"
       id="path-1-51"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.293169;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 181.02913,135.2285 c 0.005,0.005 0.0182,0.0197 0.042,0.0656 0.0115,0.0222 0.0204,0.0412 0.0372,0.0763 0.007,0.0151 0.0179,0.0372 0.0296,0.0597 0.035,0.0705 0.0717,0.15275 0.10894,0.22779 0.0356,0.0718 0.083,0.16125 0.14559,0.24893 0.0152,0.0248 0.0347,0.0503 0.0597,0.0739 0.0319,0.03 0.0711,0.0553 0.11693,0.0714 0.0449,0.0157 0.0897,0.0202 0.13101,0.0172 0.0399,-0.003 0.0751,-0.0127 0.10413,-0.0244 0.0287,-0.0115 0.0535,-0.0258 0.0743,-0.0401 0.0207,-0.0142 0.039,-0.0296 0.055,-0.0449 0.0255,-0.0244 0.0483,-0.0521 0.0675,-0.0814 0.038,-0.0491 0.0713,-0.0996 0.0972,-0.13805 0.0309,-0.0458 0.0538,-0.0784 0.0779,-0.10623 0.003,-0.003 0.006,-0.007 0.008,-0.0102 0.37414,-0.47854 0.7758,-0.85043 1.20679,-1.11337 0.12924,-0.0795 0.23833,-0.13629 0.30399,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.24178,-0.48256 c -0.0743,0.0372 -0.19817,0.10168 -0.34418,0.19152 -0.49466,0.30177 -0.94171,0.71985 -1.34624,1.23631 -0.0451,0.0529 -0.0822,0.10725 -0.11229,0.15187 -0.0333,0.0493 -0.0564,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.0153,0.0207 -0.0218,0.0318 0.004,-0.007 0.008,-0.012 0.0129,-0.0166 0.003,-0.003 0.007,-0.006 0.0133,-0.0107 0.006,-0.004 0.016,-0.0102 0.0295,-0.0156 0.0138,-0.006 0.0336,-0.0115 0.0584,-0.0133 0.026,-0.002 0.0558,9.1e-4 0.0863,0.0116 0.0312,0.0109 0.0564,0.0277 0.0753,0.0455 0.0186,0.0175 0.0292,0.0343 0.0347,0.0446 l -0.0203,-0.0324 c -0.0399,-0.0545 -0.074,-0.11682 -0.10648,-0.18229 -0.0381,-0.0769 -0.0732,-0.15567 -0.11135,-0.23255 -0.01,-0.0188 -0.0172,-0.0342 -0.0242,-0.0487 -0.0142,-0.0295 -0.0282,-0.0594 -0.0447,-0.0913 -0.0444,-0.0855 -0.0852,-0.1407 -0.12538,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 180.89474,137.67004 c 0.005,0.005 0.0182,0.0197 0.042,0.0656 0.0115,0.0223 0.0204,0.0412 0.0372,0.0763 0.007,0.0151 0.0179,0.0372 0.0296,0.0597 0.035,0.0705 0.0717,0.15275 0.10894,0.22779 0.0356,0.0718 0.083,0.16125 0.14559,0.24893 0.0152,0.0248 0.0347,0.0503 0.0597,0.0739 0.0319,0.03 0.0711,0.0553 0.11693,0.0714 0.0449,0.0157 0.0897,0.0203 0.13101,0.0172 0.0399,-0.003 0.0751,-0.0127 0.10413,-0.0244 0.0287,-0.0115 0.0535,-0.0258 0.0743,-0.0401 0.0207,-0.0142 0.039,-0.0296 0.055,-0.0449 0.0255,-0.0244 0.0483,-0.052 0.0674,-0.0813 0.038,-0.0491 0.0713,-0.0996 0.0972,-0.13805 0.0309,-0.0458 0.0538,-0.0784 0.0779,-0.10623 0.003,-0.003 0.006,-0.007 0.008,-0.0102 0.37414,-0.47854 0.7758,-0.85043 1.20679,-1.11337 0.12924,-0.0795 0.23833,-0.13629 0.30399,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.24178,-0.48256 c -0.0743,0.0372 -0.19817,0.10168 -0.34418,0.19152 -0.49466,0.30177 -0.94171,0.71985 -1.34624,1.23631 -0.0451,0.0529 -0.0822,0.10725 -0.11229,0.15187 -0.0333,0.0493 -0.0564,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.0153,0.0207 -0.0218,0.0318 0.004,-0.007 0.008,-0.012 0.0129,-0.0166 0.003,-0.003 0.007,-0.006 0.0133,-0.0107 0.006,-0.004 0.016,-0.0102 0.0295,-0.0156 0.0138,-0.006 0.0336,-0.0115 0.0584,-0.0133 0.026,-0.002 0.0558,9.1e-4 0.0863,0.0116 0.0312,0.0109 0.0564,0.0277 0.0752,0.0455 0.0186,0.0175 0.0292,0.0343 0.0347,0.0446 l -0.0203,-0.0324 c -0.0399,-0.0545 -0.074,-0.11682 -0.10648,-0.18229 -0.0381,-0.0769 -0.0732,-0.15567 -0.11135,-0.23255 -0.01,-0.0188 -0.0172,-0.0342 -0.0242,-0.0487 -0.0142,-0.0295 -0.0282,-0.0594 -0.0447,-0.0913 -0.0444,-0.0855 -0.0852,-0.1407 -0.12538,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-2"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 180.84996,140.84963 c 0.005,0.005 0.0182,0.0197 0.042,0.0656 0.0115,0.0222 0.0204,0.0412 0.0372,0.0763 0.007,0.0151 0.0179,0.0372 0.0296,0.0597 0.035,0.0705 0.0717,0.15275 0.10894,0.22779 0.0356,0.0718 0.083,0.16125 0.14559,0.24893 0.0152,0.0248 0.0347,0.0504 0.0597,0.0739 0.0319,0.03 0.0711,0.0553 0.11693,0.0714 0.0449,0.0157 0.0897,0.0203 0.13101,0.0172 0.0399,-0.003 0.0751,-0.0127 0.10413,-0.0244 0.0287,-0.0115 0.0535,-0.0258 0.0743,-0.0401 0.0207,-0.0142 0.039,-0.0296 0.055,-0.0449 0.0255,-0.0244 0.0483,-0.0521 0.0675,-0.0814 0.038,-0.0491 0.0713,-0.0996 0.0972,-0.13805 0.0309,-0.0458 0.0538,-0.0784 0.0779,-0.10623 0.003,-0.003 0.006,-0.007 0.008,-0.0102 0.37414,-0.47854 0.7758,-0.85043 1.20679,-1.11337 0.12924,-0.0795 0.23833,-0.13629 0.30399,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.24178,-0.48256 c -0.0743,0.0372 -0.19817,0.10168 -0.34418,0.19152 -0.49466,0.30177 -0.94171,0.71985 -1.34624,1.23631 -0.0451,0.0529 -0.0822,0.10725 -0.11229,0.15187 -0.0333,0.0493 -0.0564,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.0153,0.0207 -0.0218,0.0318 0.004,-0.007 0.008,-0.012 0.0129,-0.0166 0.003,-0.003 0.007,-0.006 0.0133,-0.0107 0.006,-0.004 0.016,-0.0102 0.0295,-0.0156 0.0138,-0.006 0.0336,-0.0115 0.0584,-0.0133 0.026,-0.002 0.0558,9.1e-4 0.0863,0.0116 0.0312,0.0109 0.0564,0.0277 0.0753,0.0455 0.0186,0.0175 0.0292,0.0343 0.0347,0.0446 l -0.0203,-0.0324 c -0.0399,-0.0545 -0.074,-0.11682 -0.10648,-0.18229 -0.0381,-0.0769 -0.0732,-0.15567 -0.11135,-0.23255 -0.01,-0.0188 -0.0172,-0.0342 -0.0242,-0.0487 -0.0142,-0.0295 -0.0282,-0.0594 -0.0447,-0.0913 -0.0444,-0.0855 -0.0852,-0.1407 -0.12538,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-29"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 180.80518,143.2679 c 0.005,0.005 0.0182,0.0197 0.042,0.0656 0.0115,0.0222 0.0204,0.0412 0.0372,0.0763 0.007,0.0151 0.0179,0.0372 0.0296,0.0597 0.035,0.0705 0.0717,0.15275 0.10894,0.22779 0.0356,0.0718 0.083,0.16125 0.14559,0.24893 0.0152,0.0248 0.0347,0.0503 0.0597,0.0739 0.0319,0.03 0.071,0.0553 0.11693,0.0714 0.0449,0.0157 0.0897,0.0202 0.13101,0.0172 0.0399,-0.003 0.0751,-0.0127 0.10413,-0.0244 0.0287,-0.0115 0.0535,-0.0258 0.0743,-0.0401 0.0207,-0.0142 0.039,-0.0296 0.055,-0.0449 0.0255,-0.0244 0.0483,-0.0521 0.0675,-0.0814 0.038,-0.0491 0.0713,-0.0996 0.0972,-0.13805 0.0309,-0.0458 0.0538,-0.0784 0.0779,-0.10623 0.003,-0.003 0.006,-0.007 0.008,-0.0102 0.37414,-0.47854 0.7758,-0.85043 1.20679,-1.11337 0.12924,-0.0795 0.23833,-0.13629 0.30399,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.24178,-0.48256 c -0.0743,0.0372 -0.19817,0.10168 -0.34418,0.19152 -0.49466,0.30177 -0.94171,0.71985 -1.34624,1.23631 -0.0451,0.0529 -0.0822,0.10725 -0.11229,0.15187 -0.0333,0.0493 -0.0564,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.0153,0.0207 -0.0218,0.0318 0.004,-0.007 0.008,-0.012 0.0129,-0.0166 0.003,-0.003 0.007,-0.006 0.0133,-0.0107 0.006,-0.004 0.016,-0.0102 0.0295,-0.0156 0.0138,-0.006 0.0336,-0.0115 0.0584,-0.0133 0.026,-0.002 0.0558,9.1e-4 0.0863,0.0116 0.0312,0.0109 0.0564,0.0277 0.0753,0.0455 0.0186,0.0175 0.0292,0.0343 0.0347,0.0446 l -0.0203,-0.0324 c -0.0399,-0.0545 -0.074,-0.11682 -0.10648,-0.18229 -0.0381,-0.0769 -0.0732,-0.15567 -0.11135,-0.23255 -0.01,-0.0188 -0.0172,-0.0342 -0.0242,-0.0487 -0.0142,-0.0295 -0.0282,-0.0594 -0.0447,-0.0913 -0.0444,-0.0855 -0.0852,-0.1407 -0.12538,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-9"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 180.7604,145.77574 c 0.005,0.005 0.0182,0.0197 0.042,0.0656 0.0115,0.0223 0.0204,0.0412 0.0372,0.0763 0.007,0.0151 0.0179,0.0372 0.0296,0.0597 0.035,0.0705 0.0717,0.15275 0.10894,0.22779 0.0356,0.0718 0.083,0.16125 0.14559,0.24893 0.0152,0.0249 0.0347,0.0504 0.0597,0.0739 0.0319,0.0301 0.071,0.0553 0.11693,0.0714 0.0449,0.0157 0.0897,0.0203 0.13101,0.0172 0.0399,-0.003 0.0751,-0.0127 0.10413,-0.0244 0.0287,-0.0115 0.0535,-0.0258 0.0743,-0.0401 0.0207,-0.0142 0.039,-0.0296 0.055,-0.0449 0.0255,-0.0244 0.0483,-0.0521 0.0675,-0.0813 0.038,-0.0492 0.0713,-0.0997 0.0972,-0.13805 0.0309,-0.0458 0.0538,-0.0784 0.0779,-0.10623 0.003,-0.003 0.006,-0.007 0.008,-0.0102 0.37414,-0.47854 0.7758,-0.85043 1.20679,-1.11337 0.12924,-0.0795 0.23833,-0.13629 0.30399,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.24178,-0.48256 c -0.0743,0.0372 -0.19817,0.10168 -0.34418,0.19152 -0.49466,0.30177 -0.94171,0.71985 -1.34624,1.23631 -0.0451,0.0529 -0.0822,0.10725 -0.11229,0.15187 -0.0333,0.0493 -0.0564,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.0153,0.0207 -0.0218,0.0318 0.004,-0.007 0.008,-0.012 0.0129,-0.0166 0.003,-0.003 0.007,-0.006 0.0133,-0.0107 0.006,-0.004 0.016,-0.0102 0.0295,-0.0156 0.0138,-0.006 0.0336,-0.0115 0.0584,-0.0133 0.026,-0.002 0.0558,9.1e-4 0.0863,0.0116 0.0312,0.0109 0.0564,0.0277 0.0753,0.0455 0.0186,0.0175 0.0292,0.0343 0.0347,0.0446 l -0.0203,-0.0324 c -0.0399,-0.0545 -0.074,-0.11682 -0.10648,-0.18229 -0.0381,-0.0769 -0.0732,-0.15567 -0.11135,-0.23255 -0.01,-0.0188 -0.0172,-0.0342 -0.0242,-0.0487 -0.0142,-0.0295 -0.0282,-0.0594 -0.0447,-0.0913 -0.0444,-0.0855 -0.0852,-0.1407 -0.12538,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-95"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 180.80517,149.00011 c 0.005,0.005 0.0182,0.0197 0.042,0.0656 0.0115,0.0223 0.0204,0.0412 0.0372,0.0763 0.007,0.0151 0.0179,0.0372 0.0296,0.0597 0.035,0.0705 0.0717,0.15275 0.10894,0.22779 0.0356,0.0718 0.083,0.16125 0.14559,0.24893 0.0152,0.0249 0.0347,0.0504 0.0597,0.0739 0.0319,0.03 0.071,0.0553 0.11693,0.0714 0.0449,0.0157 0.0897,0.0203 0.13101,0.0172 0.0399,-0.003 0.0751,-0.0127 0.10413,-0.0244 0.0287,-0.0115 0.0535,-0.0258 0.0743,-0.04 0.0207,-0.0142 0.039,-0.0296 0.055,-0.0449 0.0255,-0.0244 0.0483,-0.052 0.0675,-0.0813 0.038,-0.0491 0.0713,-0.0996 0.0972,-0.13805 0.0309,-0.0458 0.0538,-0.0784 0.0779,-0.10623 0.003,-0.003 0.006,-0.007 0.008,-0.0102 0.37414,-0.47854 0.7758,-0.85043 1.20679,-1.11337 0.12924,-0.0795 0.23833,-0.13629 0.30399,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.24178,-0.48256 c -0.0743,0.0372 -0.19817,0.10168 -0.34418,0.19152 -0.49466,0.30177 -0.94171,0.71985 -1.34624,1.23631 -0.0451,0.0529 -0.0822,0.10725 -0.11229,0.15187 -0.0333,0.0493 -0.0564,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.0153,0.0207 -0.0218,0.0318 0.004,-0.007 0.008,-0.012 0.0129,-0.0166 0.003,-0.003 0.007,-0.006 0.0133,-0.0107 0.006,-0.004 0.016,-0.0102 0.0295,-0.0156 0.0138,-0.006 0.0336,-0.0115 0.0584,-0.0133 0.026,-0.002 0.0558,9.1e-4 0.0863,0.0116 0.0312,0.0109 0.0564,0.0277 0.0753,0.0455 0.0186,0.0175 0.0292,0.0343 0.0347,0.0446 l -0.0203,-0.0324 c -0.0399,-0.0545 -0.074,-0.11682 -0.10648,-0.18229 -0.0381,-0.0769 -0.0732,-0.15567 -0.11135,-0.23255 -0.01,-0.0188 -0.0172,-0.0342 -0.0242,-0.0487 -0.0142,-0.0295 -0.0282,-0.0594 -0.0447,-0.0913 -0.0444,-0.0855 -0.0852,-0.1407 -0.12538,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-4"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 180.80517,151.46316 c 0.005,0.005 0.0182,0.0197 0.042,0.0656 0.0115,0.0222 0.0204,0.0412 0.0372,0.0763 0.007,0.0151 0.0179,0.0372 0.0296,0.0597 0.035,0.0705 0.0717,0.15275 0.10894,0.22779 0.0356,0.0718 0.083,0.16125 0.14559,0.24893 0.0152,0.0248 0.0347,0.0504 0.0597,0.0739 0.0319,0.0301 0.071,0.0553 0.11693,0.0714 0.0449,0.0157 0.0897,0.0203 0.13101,0.0172 0.0399,-0.003 0.0751,-0.0127 0.10413,-0.0244 0.0287,-0.0115 0.0535,-0.0258 0.0743,-0.0401 0.0207,-0.0142 0.039,-0.0296 0.055,-0.0449 0.0255,-0.0244 0.0483,-0.0521 0.0675,-0.0814 0.038,-0.0491 0.0713,-0.0996 0.0972,-0.13805 0.0309,-0.0458 0.0538,-0.0784 0.0779,-0.10623 0.003,-0.003 0.006,-0.007 0.008,-0.0102 0.37414,-0.47854 0.7758,-0.85043 1.20679,-1.11337 0.12924,-0.0795 0.23833,-0.13629 0.30399,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.24178,-0.48256 c -0.0743,0.0372 -0.19817,0.10168 -0.34418,0.19152 -0.49466,0.30177 -0.94171,0.71985 -1.34624,1.23631 -0.0451,0.0529 -0.0822,0.10725 -0.11229,0.15187 -0.0333,0.0493 -0.0564,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.0153,0.0207 -0.0218,0.0318 0.004,-0.007 0.008,-0.012 0.0129,-0.0166 0.003,-0.003 0.007,-0.006 0.0133,-0.0107 0.006,-0.004 0.016,-0.0102 0.0295,-0.0156 0.0138,-0.006 0.0336,-0.0115 0.0584,-0.0133 0.026,-0.002 0.0558,9.1e-4 0.0863,0.0116 0.0312,0.0109 0.0564,0.0277 0.0753,0.0455 0.0186,0.0175 0.0292,0.0343 0.0347,0.0446 l -0.0203,-0.0324 c -0.0399,-0.0545 -0.074,-0.11682 -0.10648,-0.18229 -0.0381,-0.0769 -0.0732,-0.15567 -0.11135,-0.23255 -0.01,-0.0188 -0.0172,-0.0342 -0.0242,-0.0487 -0.0142,-0.0295 -0.0282,-0.0594 -0.0447,-0.0913 -0.0444,-0.0855 -0.0852,-0.1407 -0.12538,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-93"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 180.80518,154.37405 c 0.005,0.005 0.0182,0.0197 0.042,0.0656 0.0115,0.0223 0.0204,0.0412 0.0372,0.0763 0.007,0.0151 0.0179,0.0372 0.0296,0.0597 0.035,0.0705 0.0717,0.15275 0.10894,0.22779 0.0356,0.0718 0.083,0.16125 0.14559,0.24893 0.0152,0.0249 0.0347,0.0504 0.0597,0.0739 0.0319,0.0301 0.071,0.0553 0.11693,0.0714 0.0449,0.0157 0.0897,0.0203 0.13101,0.0172 0.0399,-0.003 0.0751,-0.0127 0.10413,-0.0244 0.0287,-0.0115 0.0535,-0.0258 0.0743,-0.0401 0.0207,-0.0142 0.039,-0.0296 0.055,-0.0449 0.0255,-0.0244 0.0483,-0.0521 0.0675,-0.0813 0.038,-0.0491 0.0713,-0.0996 0.0972,-0.13805 0.0309,-0.0458 0.0538,-0.0784 0.0779,-0.10623 0.003,-0.003 0.006,-0.007 0.008,-0.0102 0.37414,-0.47854 0.7758,-0.85043 1.20679,-1.11337 0.12924,-0.0795 0.23833,-0.13629 0.30399,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.24178,-0.48256 c -0.0743,0.0372 -0.19817,0.10168 -0.34418,0.19152 -0.49466,0.30177 -0.94171,0.71985 -1.34624,1.23631 -0.0451,0.0529 -0.0822,0.10725 -0.11229,0.15187 -0.0333,0.0493 -0.0564,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.0153,0.0207 -0.0218,0.0318 0.004,-0.007 0.008,-0.012 0.0129,-0.0166 0.003,-0.003 0.007,-0.006 0.0133,-0.0107 0.006,-0.004 0.016,-0.0102 0.0295,-0.0156 0.0138,-0.006 0.0336,-0.0115 0.0584,-0.0133 0.026,-0.002 0.0558,9.1e-4 0.0863,0.0116 0.0312,0.0109 0.0564,0.0277 0.0753,0.0455 0.0186,0.0175 0.0292,0.0343 0.0347,0.0446 l -0.0203,-0.0324 c -0.0399,-0.0545 -0.074,-0.11682 -0.10648,-0.18229 -0.0381,-0.0769 -0.0732,-0.15567 -0.11135,-0.23255 -0.01,-0.0188 -0.0172,-0.0342 -0.0242,-0.0487 -0.0142,-0.0295 -0.0282,-0.0594 -0.0447,-0.0913 -0.0444,-0.0855 -0.0852,-0.1407 -0.12538,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-92"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 180.80517,156.92668 c 0.005,0.005 0.0182,0.0197 0.042,0.0656 0.0115,0.0223 0.0204,0.0412 0.0372,0.0763 0.007,0.0151 0.0179,0.0372 0.0296,0.0597 0.035,0.0705 0.0717,0.15275 0.10894,0.22779 0.0356,0.0718 0.083,0.16125 0.14559,0.24893 0.0152,0.0249 0.0347,0.0504 0.0597,0.0739 0.0319,0.03 0.071,0.0553 0.11693,0.0714 0.0449,0.0157 0.0897,0.0203 0.13101,0.0172 0.0399,-0.003 0.0751,-0.0127 0.10413,-0.0244 0.0287,-0.0115 0.0535,-0.0258 0.0743,-0.04 0.0207,-0.0142 0.039,-0.0296 0.055,-0.0449 0.0255,-0.0244 0.0483,-0.052 0.0675,-0.0813 0.038,-0.0491 0.0713,-0.0996 0.0972,-0.13805 0.0309,-0.0458 0.0538,-0.0784 0.0779,-0.10623 0.003,-0.003 0.006,-0.007 0.008,-0.0102 0.37414,-0.47854 0.7758,-0.85043 1.20679,-1.11337 0.12924,-0.0795 0.23833,-0.13629 0.30399,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.24178,-0.48256 c -0.0743,0.0372 -0.19817,0.10168 -0.34418,0.19152 -0.49466,0.30177 -0.94171,0.71985 -1.34624,1.23631 -0.0451,0.0529 -0.0822,0.10725 -0.11229,0.15187 -0.0333,0.0493 -0.0564,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.0153,0.0207 -0.0218,0.0318 0.004,-0.007 0.008,-0.012 0.0129,-0.0166 0.003,-0.003 0.007,-0.006 0.0133,-0.0107 0.006,-0.004 0.016,-0.0102 0.0295,-0.0156 0.0138,-0.006 0.0336,-0.0115 0.0584,-0.0133 0.026,-0.002 0.0558,9.1e-4 0.0863,0.0116 0.0312,0.0109 0.0564,0.0277 0.0753,0.0455 0.0186,0.0175 0.0292,0.0343 0.0347,0.0446 l -0.0203,-0.0324 c -0.0399,-0.0545 -0.074,-0.11682 -0.10648,-0.18229 -0.0381,-0.0769 -0.0732,-0.15567 -0.11135,-0.23255 -0.01,-0.0188 -0.0172,-0.0342 -0.0242,-0.0487 -0.0142,-0.0295 -0.0282,-0.0594 -0.0447,-0.0913 -0.0444,-0.0855 -0.0852,-0.1407 -0.12538,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-91"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 48.534495,294.77252 c 0.0047,0.005 0.01821,0.0197 0.042,0.0656 0.01154,0.0223 0.02036,0.0412 0.03724,0.0763 0.0073,0.0151 0.01794,0.0372 0.02963,0.0597 0.03497,0.0705 0.07168,0.15277 0.108952,0.2278 0.03561,0.0718 0.08302,0.16125 0.145585,0.24893 0.01521,0.0248 0.03469,0.0503 0.05969,0.0739 0.03187,0.0301 0.07104,0.0554 0.116928,0.0714 0.04492,0.0157 0.08969,0.0203 0.131017,0.0172 0.03993,-0.003 0.07507,-0.0127 0.104131,-0.0244 0.02866,-0.0115 0.05347,-0.0258 0.07426,-0.0401 0.02068,-0.0142 0.03901,-0.0296 0.05501,-0.0449 0.02545,-0.0244 0.0483,-0.0521 0.06745,-0.0813 0.03801,-0.0491 0.07131,-0.0996 0.09721,-0.13805 0.0309,-0.0458 0.05381,-0.0784 0.07787,-0.10623 0.0029,-0.003 0.0057,-0.007 0.0084,-0.0102 0.374153,-0.47854 0.775807,-0.85043 1.206801,-1.11337 0.129233,-0.0795 0.238333,-0.13629 0.303987,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.241778,-0.48256 c -0.07429,0.0372 -0.198183,0.10169 -0.344185,0.19152 -0.494655,0.30177 -0.941702,0.71985 -1.346243,1.23631 -0.04509,0.0529 -0.08219,0.10725 -0.112286,0.15187 -0.03328,0.0493 -0.05635,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.01529,0.0207 -0.02178,0.0318 0.0042,-0.007 0.0082,-0.012 0.01295,-0.0166 0.0027,-0.003 0.0071,-0.006 0.0133,-0.0107 0.0062,-0.004 0.01598,-0.0102 0.02954,-0.0156 0.01376,-0.006 0.03356,-0.0115 0.05842,-0.0133 0.02601,-0.002 0.05579,9.1e-4 0.08632,0.0116 0.03122,0.0109 0.05643,0.0277 0.07526,0.0455 0.01858,0.0175 0.0292,0.0343 0.03469,0.0446 l -0.02034,-0.0324 c -0.03986,-0.0545 -0.07399,-0.11681 -0.10648,-0.18228 -0.03815,-0.0769 -0.07321,-0.15567 -0.11136,-0.23255 -0.0097,-0.0188 -0.01723,-0.0342 -0.02417,-0.0487 -0.01416,-0.0295 -0.02816,-0.0594 -0.04471,-0.0913 -0.04437,-0.0855 -0.08516,-0.1407 -0.125376,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-5"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 69.434239,303.74323 c 0.0047,0.005 0.01821,0.0197 0.042,0.0656 0.01154,0.0222 0.02036,0.0412 0.03724,0.0763 0.0073,0.0151 0.01794,0.0372 0.02963,0.0597 0.03497,0.0705 0.07168,0.15277 0.108952,0.2278 0.03561,0.0718 0.08302,0.16125 0.145585,0.24893 0.01521,0.0248 0.03469,0.0503 0.05969,0.0739 0.03187,0.0301 0.07104,0.0554 0.116928,0.0714 0.04492,0.0157 0.08969,0.0202 0.131017,0.0172 0.03993,-0.003 0.07507,-0.0127 0.104131,-0.0244 0.02866,-0.0115 0.05347,-0.0258 0.07426,-0.0401 0.02068,-0.0142 0.03901,-0.0296 0.05501,-0.0449 0.02545,-0.0244 0.0483,-0.0521 0.06745,-0.0813 0.03801,-0.0491 0.07131,-0.0996 0.09721,-0.13805 0.0309,-0.0458 0.05381,-0.0784 0.07788,-0.10623 0.0029,-0.003 0.0057,-0.007 0.0084,-0.0102 0.374153,-0.47854 0.775807,-0.85043 1.206801,-1.11337 0.129233,-0.0795 0.238333,-0.13629 0.303987,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.241778,-0.48256 c -0.0743,0.0372 -0.198183,0.10169 -0.344185,0.19152 -0.494655,0.30177 -0.941702,0.71985 -1.346243,1.23631 -0.04509,0.0529 -0.08219,0.10725 -0.112286,0.15187 -0.03328,0.0493 -0.05635,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.01529,0.0207 -0.02178,0.0318 0.0042,-0.007 0.0082,-0.012 0.01295,-0.0166 0.0027,-0.003 0.0071,-0.006 0.0133,-0.0107 0.0062,-0.004 0.01598,-0.0102 0.02954,-0.0156 0.01376,-0.006 0.03356,-0.0115 0.05842,-0.0133 0.02601,-0.002 0.05579,9.1e-4 0.08632,0.0116 0.03123,0.0109 0.05643,0.0277 0.07526,0.0455 0.01858,0.0175 0.0292,0.0343 0.03469,0.0446 l -0.02034,-0.0324 c -0.03986,-0.0545 -0.07399,-0.11681 -0.10648,-0.18228 -0.03815,-0.0769 -0.07321,-0.15567 -0.11136,-0.23255 -0.0097,-0.0188 -0.01723,-0.0342 -0.02417,-0.0487 -0.01416,-0.0295 -0.02816,-0.0594 -0.04471,-0.0913 -0.04437,-0.0855 -0.08516,-0.1407 -0.125376,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-5-4"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 16.331608,311.95395 c 0.0047,0.005 0.01821,0.0197 0.042,0.0656 0.01155,0.0222 0.02036,0.0412 0.03724,0.0763 0.0073,0.0151 0.01794,0.0372 0.02963,0.0597 0.03497,0.0705 0.07168,0.15277 0.108952,0.2278 0.03561,0.0718 0.08302,0.16125 0.145585,0.24893 0.01521,0.0249 0.03469,0.0503 0.05969,0.0739 0.03187,0.0301 0.07105,0.0553 0.116928,0.0714 0.04492,0.0157 0.08969,0.0202 0.131017,0.0172 0.03993,-0.003 0.07507,-0.0127 0.104131,-0.0244 0.02866,-0.0115 0.05347,-0.0258 0.07426,-0.04 0.02068,-0.0142 0.03901,-0.0296 0.05501,-0.0449 0.02545,-0.0244 0.0483,-0.052 0.06745,-0.0813 0.03801,-0.0491 0.07131,-0.0996 0.09721,-0.13805 0.03089,-0.0458 0.05381,-0.0784 0.07787,-0.10623 0.0029,-0.003 0.0057,-0.007 0.0084,-0.0102 0.374153,-0.47854 0.775807,-0.85043 1.206801,-1.11337 0.129233,-0.0795 0.238333,-0.13629 0.303987,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.241778,-0.48256 c -0.07429,0.0372 -0.198183,0.10169 -0.344185,0.19152 -0.494655,0.30177 -0.941702,0.71985 -1.346243,1.23631 -0.04509,0.0529 -0.08219,0.10725 -0.112286,0.15187 -0.03328,0.0493 -0.05635,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.01529,0.0207 -0.02178,0.0318 0.0042,-0.007 0.0082,-0.012 0.01295,-0.0166 0.0027,-0.003 0.0071,-0.006 0.0133,-0.0107 0.0062,-0.004 0.01598,-0.0102 0.02954,-0.0156 0.01376,-0.006 0.03356,-0.0115 0.05842,-0.0133 0.02601,-0.002 0.05579,9.1e-4 0.08632,0.0116 0.03122,0.0109 0.05643,0.0277 0.07526,0.0455 0.01858,0.0175 0.0292,0.0343 0.03469,0.0446 l -0.02034,-0.0324 c -0.03986,-0.0545 -0.07399,-0.11681 -0.10648,-0.18228 -0.03815,-0.0769 -0.07321,-0.15567 -0.11136,-0.23255 -0.0097,-0.0188 -0.01723,-0.0342 -0.02417,-0.0487 -0.01416,-0.0295 -0.02816,-0.0594 -0.04471,-0.0913 -0.04437,-0.0855 -0.08516,-0.1407 -0.125376,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-5-6"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 16.339061,315.13595 c 0.0047,0.005 0.01821,0.0197 0.042,0.0656 0.01155,0.0222 0.02036,0.0412 0.03724,0.0763 0.0073,0.0151 0.01794,0.0372 0.02963,0.0597 0.03497,0.0705 0.07168,0.15277 0.108952,0.2278 0.03561,0.0718 0.08302,0.16125 0.145585,0.24893 0.0152,0.0248 0.03469,0.0503 0.05969,0.0739 0.03187,0.0301 0.07104,0.0554 0.116928,0.0714 0.04492,0.0157 0.08969,0.0202 0.131017,0.0172 0.03993,-0.003 0.07507,-0.0127 0.104131,-0.0244 0.02866,-0.0115 0.05347,-0.0258 0.07426,-0.0401 0.02068,-0.0142 0.03901,-0.0296 0.05501,-0.0449 0.02545,-0.0244 0.0483,-0.0521 0.06745,-0.0813 0.03801,-0.0491 0.07131,-0.0996 0.09721,-0.13805 0.0309,-0.0458 0.05381,-0.0784 0.07787,-0.10623 0.0029,-0.003 0.0057,-0.007 0.0084,-0.0102 0.374153,-0.47854 0.775807,-0.85043 1.206801,-1.11337 0.129233,-0.0795 0.238333,-0.13629 0.303987,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.241778,-0.48256 c -0.07429,0.0372 -0.198183,0.10169 -0.344185,0.19152 -0.494655,0.30177 -0.941702,0.71985 -1.346243,1.23631 -0.04509,0.0529 -0.08219,0.10725 -0.112286,0.15187 -0.03328,0.0493 -0.05635,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.01529,0.0207 -0.02178,0.0318 0.0042,-0.007 0.0082,-0.012 0.01295,-0.0166 0.0028,-0.003 0.0071,-0.006 0.0133,-0.0107 0.0062,-0.004 0.01598,-0.0102 0.02954,-0.0156 0.01376,-0.006 0.03356,-0.0115 0.05842,-0.0133 0.02601,-0.002 0.05579,9.1e-4 0.08632,0.0116 0.03122,0.0109 0.05643,0.0277 0.07526,0.0455 0.01858,0.0175 0.0292,0.0343 0.03469,0.0446 l -0.02034,-0.0324 c -0.03986,-0.0545 -0.07399,-0.11681 -0.10648,-0.18228 -0.03815,-0.0769 -0.07321,-0.15567 -0.11136,-0.23255 -0.0097,-0.0188 -0.01723,-0.0342 -0.02417,-0.0487 -0.01416,-0.0295 -0.02816,-0.0594 -0.04471,-0.0913 -0.04437,-0.0855 -0.08516,-0.1407 -0.125376,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-5-68"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 16.302192,318.21301 c 0.0047,0.005 0.01821,0.0197 0.042,0.0656 0.01154,0.0223 0.02036,0.0412 0.03724,0.0763 0.0073,0.0151 0.01794,0.0372 0.02963,0.0597 0.03497,0.0705 0.07168,0.15277 0.108952,0.2278 0.03561,0.0718 0.08302,0.16125 0.145585,0.24893 0.01521,0.0249 0.03469,0.0504 0.05969,0.0739 0.03187,0.0301 0.07105,0.0553 0.116928,0.0714 0.04492,0.0157 0.08969,0.0203 0.131017,0.0172 0.03993,-0.003 0.07507,-0.0127 0.104131,-0.0244 0.02866,-0.0115 0.05347,-0.0258 0.07426,-0.0401 0.02068,-0.0142 0.03901,-0.0296 0.05501,-0.0449 0.02545,-0.0244 0.0483,-0.0521 0.06745,-0.0813 0.03801,-0.0491 0.07131,-0.0996 0.09721,-0.13805 0.0309,-0.0458 0.05381,-0.0784 0.07787,-0.10623 0.0029,-0.003 0.0057,-0.007 0.0084,-0.0102 0.374153,-0.47854 0.775807,-0.85043 1.206801,-1.11337 0.129233,-0.0795 0.238333,-0.13629 0.303987,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.241778,-0.48256 c -0.07429,0.0372 -0.198183,0.10169 -0.344185,0.19152 -0.494655,0.30177 -0.941702,0.71985 -1.346243,1.23631 -0.04509,0.0529 -0.08219,0.10725 -0.112286,0.15187 -0.03328,0.0493 -0.05635,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.01529,0.0207 -0.02178,0.0318 0.0042,-0.007 0.0082,-0.012 0.01295,-0.0166 0.0028,-0.003 0.0071,-0.006 0.0133,-0.0107 0.0062,-0.004 0.01598,-0.0102 0.02954,-0.0156 0.01376,-0.006 0.03356,-0.0115 0.05842,-0.0133 0.02601,-0.002 0.05579,9.1e-4 0.08632,0.0116 0.03122,0.0109 0.05643,0.0277 0.07526,0.0455 0.01858,0.0175 0.0292,0.0343 0.03469,0.0446 l -0.02034,-0.0324 c -0.03986,-0.0545 -0.07399,-0.11681 -0.10648,-0.18228 -0.03815,-0.0769 -0.07321,-0.15567 -0.11136,-0.23255 -0.0097,-0.0188 -0.01723,-0.0342 -0.02417,-0.0487 -0.01416,-0.0295 -0.02816,-0.0594 -0.04471,-0.0913 -0.04437,-0.0855 -0.08516,-0.1407 -0.125376,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-5-1"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 16.339061,321.34968 c 0.0047,0.005 0.01821,0.0197 0.042,0.0656 0.01155,0.0222 0.02036,0.0412 0.03724,0.0763 0.0073,0.0151 0.01794,0.0372 0.02963,0.0597 0.03497,0.0705 0.07168,0.15277 0.108952,0.2278 0.03561,0.0718 0.08302,0.16125 0.145585,0.24893 0.0152,0.0248 0.03469,0.0503 0.05969,0.0739 0.03187,0.0301 0.07104,0.0554 0.116928,0.0714 0.04492,0.0157 0.08969,0.0202 0.131017,0.0172 0.03993,-0.003 0.07507,-0.0127 0.104131,-0.0244 0.02866,-0.0115 0.05347,-0.0258 0.07426,-0.0401 0.02068,-0.0142 0.03901,-0.0296 0.05501,-0.0449 0.02545,-0.0244 0.0483,-0.0521 0.06745,-0.0813 0.03801,-0.0491 0.07131,-0.0996 0.09721,-0.13805 0.0309,-0.0458 0.05381,-0.0784 0.07787,-0.10623 0.0029,-0.003 0.0057,-0.007 0.0084,-0.0102 0.374153,-0.47854 0.775807,-0.85043 1.206801,-1.11337 0.129233,-0.0795 0.238333,-0.13629 0.303987,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.241778,-0.48256 c -0.07429,0.0372 -0.198183,0.10169 -0.344185,0.19152 -0.494655,0.30177 -0.941702,0.71985 -1.346243,1.23631 -0.04509,0.0529 -0.08219,0.10725 -0.112286,0.15187 -0.03328,0.0493 -0.05635,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.01529,0.0207 -0.02178,0.0318 0.0042,-0.007 0.0082,-0.012 0.01295,-0.0166 0.0028,-0.003 0.0071,-0.006 0.0133,-0.0107 0.0062,-0.004 0.01598,-0.0102 0.02954,-0.0156 0.01376,-0.006 0.03356,-0.0115 0.05842,-0.0133 0.02601,-0.002 0.05579,9.1e-4 0.08632,0.0116 0.03122,0.0109 0.05643,0.0277 0.07526,0.0455 0.01858,0.0175 0.0292,0.0343 0.03469,0.0446 l -0.02034,-0.0324 c -0.03986,-0.0545 -0.07399,-0.11681 -0.10648,-0.18228 -0.03815,-0.0769 -0.07321,-0.15567 -0.11136,-0.23255 -0.0097,-0.0188 -0.01723,-0.0342 -0.02417,-0.0487 -0.01416,-0.0295 -0.02816,-0.0594 -0.04471,-0.0913 -0.04437,-0.0855 -0.08516,-0.1407 -0.125376,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-5-3"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 16.257409,324.76964 c 0.0047,0.005 0.01821,0.0197 0.042,0.0656 0.01154,0.0222 0.02036,0.0412 0.03724,0.0763 0.0073,0.0151 0.01794,0.0372 0.02963,0.0597 0.03497,0.0705 0.07168,0.15277 0.108952,0.2278 0.03561,0.0718 0.08302,0.16125 0.145585,0.24893 0.01521,0.0248 0.03469,0.0503 0.05969,0.0739 0.03187,0.0301 0.07105,0.0554 0.116928,0.0714 0.04492,0.0157 0.08969,0.0202 0.131017,0.0172 0.03993,-0.003 0.07507,-0.0127 0.104131,-0.0244 0.02866,-0.0115 0.05347,-0.0258 0.07426,-0.0401 0.02068,-0.0142 0.03901,-0.0296 0.05501,-0.0449 0.02545,-0.0244 0.0483,-0.0521 0.06745,-0.0813 0.03801,-0.0491 0.07131,-0.0996 0.09721,-0.13805 0.03089,-0.0458 0.05381,-0.0784 0.07787,-0.10623 0.0029,-0.003 0.0057,-0.007 0.0084,-0.0102 0.374153,-0.47854 0.775807,-0.85043 1.206801,-1.11337 0.129233,-0.0795 0.238333,-0.13629 0.303987,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.241778,-0.48256 c -0.07429,0.0372 -0.198183,0.10169 -0.344185,0.19152 -0.494655,0.30177 -0.941702,0.71985 -1.346243,1.23631 -0.04509,0.0529 -0.08219,0.10725 -0.112286,0.15187 -0.03328,0.0493 -0.05635,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.01529,0.0207 -0.02178,0.0318 0.0042,-0.007 0.0082,-0.012 0.01295,-0.0166 0.0027,-0.003 0.0071,-0.006 0.0133,-0.0107 0.0062,-0.004 0.01598,-0.0102 0.02954,-0.0156 0.01376,-0.006 0.03356,-0.0115 0.05842,-0.0133 0.02601,-0.002 0.05579,9.1e-4 0.08632,0.0116 0.03122,0.0109 0.05643,0.0277 0.07526,0.0455 0.01858,0.0175 0.0292,0.0343 0.03469,0.0446 l -0.02034,-0.0324 c -0.03986,-0.0545 -0.07399,-0.11681 -0.10648,-0.18228 -0.03815,-0.0769 -0.07321,-0.15567 -0.11136,-0.23255 -0.0097,-0.0188 -0.01723,-0.0342 -0.02417,-0.0487 -0.01416,-0.0295 -0.02816,-0.0594 -0.04471,-0.0913 -0.04437,-0.0855 -0.08516,-0.1407 -0.125376,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-5-47"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 87.800676,303.61657 c 0.0047,0.005 0.01821,0.0197 0.042,0.0656 0.01154,0.0222 0.02036,0.0412 0.03724,0.0763 0.0073,0.0151 0.01794,0.0372 0.02963,0.0597 0.03497,0.0705 0.07168,0.15277 0.108952,0.2278 0.03561,0.0718 0.08302,0.16125 0.145585,0.24893 0.0152,0.0249 0.03469,0.0503 0.05969,0.0739 0.03187,0.0301 0.07104,0.0553 0.116928,0.0714 0.04492,0.0157 0.08969,0.0202 0.131017,0.0172 0.03993,-0.003 0.07507,-0.0127 0.104131,-0.0244 0.02866,-0.0115 0.05347,-0.0258 0.07426,-0.0401 0.02068,-0.0142 0.03901,-0.0296 0.05501,-0.0449 0.02545,-0.0244 0.0483,-0.0521 0.06745,-0.0813 0.03801,-0.0491 0.07131,-0.0996 0.09721,-0.13805 0.0309,-0.0458 0.05381,-0.0784 0.07787,-0.10623 0.0029,-0.003 0.0057,-0.007 0.0084,-0.0102 0.374153,-0.47854 0.775807,-0.85043 1.206801,-1.11337 0.129233,-0.0795 0.238333,-0.13629 0.303987,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.241778,-0.48256 c -0.07429,0.0372 -0.198183,0.10169 -0.344185,0.19152 -0.494655,0.30177 -0.941702,0.71985 -1.346243,1.23631 -0.04509,0.0529 -0.08219,0.10725 -0.112286,0.15187 -0.03328,0.0493 -0.05635,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.01529,0.0207 -0.02178,0.0318 0.0042,-0.007 0.0082,-0.012 0.01295,-0.0166 0.0028,-0.003 0.0071,-0.006 0.0133,-0.0107 0.0062,-0.004 0.01598,-0.0102 0.02954,-0.0156 0.01376,-0.006 0.03356,-0.0115 0.05842,-0.0133 0.02601,-0.002 0.05579,9.1e-4 0.08632,0.0116 0.03122,0.0109 0.05643,0.0277 0.07526,0.0455 0.01858,0.0175 0.0292,0.0343 0.03469,0.0446 l -0.02034,-0.0324 c -0.03986,-0.0545 -0.07399,-0.11681 -0.10648,-0.18228 -0.03815,-0.0769 -0.07321,-0.15567 -0.11136,-0.23255 -0.0097,-0.0188 -0.01723,-0.0342 -0.02417,-0.0487 -0.01416,-0.0295 -0.02816,-0.0594 -0.04471,-0.0913 -0.04437,-0.0855 -0.08516,-0.1407 -0.125376,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-5-0"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 154.29985,294.89919 c 0.005,0.005 0.0182,0.0197 0.042,0.0656 0.0115,0.0222 0.0204,0.0412 0.0372,0.0763 0.007,0.0151 0.018,0.0372 0.0296,0.0597 0.035,0.0705 0.0717,0.15275 0.10894,0.22779 0.0356,0.0718 0.083,0.16125 0.14559,0.24893 0.0152,0.0248 0.0347,0.0503 0.0597,0.0739 0.0319,0.0301 0.0711,0.0553 0.11693,0.0714 0.0449,0.0157 0.0897,0.0202 0.13101,0.0172 0.0399,-0.003 0.0751,-0.0127 0.10413,-0.0244 0.0287,-0.0115 0.0535,-0.0258 0.0743,-0.0401 0.0207,-0.0142 0.039,-0.0296 0.055,-0.0449 0.0255,-0.0244 0.0483,-0.0521 0.0675,-0.0813 0.038,-0.0491 0.0713,-0.0996 0.0972,-0.13805 0.0309,-0.0458 0.0538,-0.0784 0.0779,-0.10623 0.003,-0.003 0.006,-0.007 0.008,-0.0102 0.37414,-0.47854 0.7758,-0.85043 1.20679,-1.11337 0.12924,-0.0795 0.23833,-0.13629 0.30399,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.24178,-0.48256 c -0.0743,0.0372 -0.19817,0.10168 -0.34418,0.19152 -0.49466,0.30177 -0.94171,0.71985 -1.34624,1.23631 -0.0451,0.0529 -0.0822,0.10725 -0.11229,0.15187 -0.0333,0.0493 -0.0564,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.0153,0.0207 -0.0218,0.0318 0.004,-0.007 0.008,-0.012 0.0129,-0.0166 0.003,-0.003 0.007,-0.006 0.0133,-0.0107 0.006,-0.004 0.016,-0.0102 0.0295,-0.0156 0.0138,-0.006 0.0336,-0.0115 0.0584,-0.0133 0.026,-0.002 0.0558,9.1e-4 0.0863,0.0116 0.0312,0.0109 0.0564,0.0277 0.0752,0.0455 0.0186,0.0175 0.0292,0.0343 0.0347,0.0446 l -0.0203,-0.0324 c -0.0399,-0.0545 -0.074,-0.11682 -0.10648,-0.18229 -0.0381,-0.0769 -0.0732,-0.15567 -0.11135,-0.23255 -0.01,-0.0188 -0.0172,-0.0342 -0.0242,-0.0487 -0.0142,-0.0295 -0.0282,-0.0594 -0.0447,-0.0913 -0.0444,-0.0855 -0.0852,-0.1407 -0.12538,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-5-7"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 57.09705,298.90505 c 0.0063,0.006 0.02678,0.0254 0.06456,0.0903 0.0184,0.0316 0.03279,0.059 0.06012,0.10979 0.01174,0.0218 0.02917,0.054 0.0481,0.0866 0.04163,0.075 0.09574,0.18293 0.169898,0.31511 0.05591,0.0996 0.130487,0.22412 0.227702,0.34482 0.02481,0.0355 0.0556,0.0708 0.09369,0.10283 0.04792,0.0403 0.104262,0.0726 0.167602,0.0929 0.06188,0.0199 0.123098,0.026 0.179953,0.0227 0.0552,-0.003 0.104638,-0.0151 0.146697,-0.0301 0.08052,-0.0288 0.145083,-0.0728 0.192508,-0.11332 0.03991,-0.0341 0.07563,-0.0725 0.105968,-0.11275 0.06069,-0.0695 0.114239,-0.14162 0.15532,-0.19572 0.04877,-0.0642 0.0843,-0.10906 0.121017,-0.14683 0.0047,-0.005 0.0092,-0.01 0.01362,-0.0147 0.590137,-0.67125 1.220867,-1.18543 1.876839,-1.54408 0.214261,-0.11828 0.395434,-0.20217 0.50363,-0.25034 a 0.39974936,0.39974936 90 0 0 -0.32519,-0.73038 c -0.120719,0.0537 -0.323991,0.14784 -0.563409,0.28001 -0.74536,0.40751 -1.445217,0.98228 -2.086143,1.70989 -0.07081,0.0739 -0.129688,0.15053 -0.177089,0.21295 -0.05264,0.0693 -0.08861,0.11752 -0.128433,0.16199 -0.01119,0.0125 -0.02158,0.0257 -0.03111,0.0395 0.0047,-0.007 0.0092,-0.0119 0.01558,-0.0173 0.0054,-0.005 0.02388,-0.0196 0.05791,-0.0318 0.01839,-0.007 0.04413,-0.0133 0.07602,-0.0151 0.03317,-0.002 0.07117,0.002 0.110687,0.0143 0.04055,0.013 0.07507,0.0333 0.102489,0.0563 0.02726,0.0229 0.04427,0.0458 0.05404,0.0617 l -0.0321,-0.0449 c -0.0589,-0.0713 -0.110552,-0.15455 -0.160555,-0.24367 -0.06069,-0.10816 -0.117579,-0.2209 -0.172165,-0.31905 -0.01564,-0.027 -0.02782,-0.0494 -0.03914,-0.0705 -0.02304,-0.0428 -0.04611,-0.0866 -0.07315,-0.13305 -0.07272,-0.12489 -0.138793,-0.2046 -0.203356,-0.26624 a 0.39974936,0.39974936 90 0 0 -0.552112,0.57824 z"
       id="path-1-8-26"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.344125;stroke-dasharray:none;stroke-opacity:1" />
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="72.199097"
       y="295.12967"
       id="text38817"><tspan
         id="tspan38815"
         style="stroke-width:0.306"
         x="72.199097"
         y="295.12967">878999999999999</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="76.379044"
       y="299.43625"
       id="text38821"><tspan
         id="tspan38819"
         style="stroke-width:0.306"
         x="76.379044"
         y="299.43625">COMENTARIO CUALES</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="106.52534"
       y="303.61618"
       id="text38825"><tspan
         id="tspan38823"
         style="stroke-width:0.306"
         x="106.52534"
         y="303.61618">OTRA 2</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="24.317099"
       y="312.1366"
       id="text38973"><tspan
         id="tspan38971"
         style="stroke-width:0.306"
         x="24.317099"
         y="312.1366">01</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="24.329475"
       y="315.64334"
       id="text38973-9"><tspan
         id="tspan38971-1"
         style="stroke-width:0.306"
         x="24.329475"
         y="315.64334">01</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="24.342592"
       y="318.91248"
       id="text38973-91"><tspan
         id="tspan38971-3"
         style="stroke-width:0.306"
         x="24.342592"
         y="318.91248">01</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="24.329475"
       y="322.09207"
       id="text38973-0"><tspan
         id="tspan38971-8"
         style="stroke-width:0.306"
         x="24.329475"
         y="322.09207">01</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="24.316359"
       y="325.09253"
       id="text38973-3"><tspan
         id="tspan38971-4"
         style="stroke-width:0.306"
         x="24.316359"
         y="325.09253">01</tspan></text>
    <path
       d="m 122.23791,314.64488 c -0.055,0.52932 -0.005,1.12859 0.24463,1.74571 0.19534,0.48325 0.49887,0.94132 0.90824,1.35277 0.35095,0.35274 0.77373,0.66485 1.25114,0.91975 0.42318,0.22595 0.89402,0.40912 1.38757,0.5273 1.49019,0.39544 3.04886,0.58561 4.7346,0.64679 1.51964,0.0552 3.00444,0.003 4.59415,-0.0513 0.78422,0.0246 1.65357,-0.10789 2.44763,-0.49787 0.36449,-0.17901 0.71759,-0.41487 1.03363,-0.71822 0.0221,-0.0212 0.0441,-0.0429 0.066,-0.0649 0.30907,-0.31126 0.58996,-0.70077 0.79718,-1.18 0.0457,-0.0998 0.0948,-0.15985 0.0728,-0.13553 -0.006,0.007 -0.0447,0.0488 -0.12105,0.0945 -0.0391,0.0233 -0.0941,0.0512 -0.16459,0.0741 -0.0701,0.0228 -0.15836,0.0414 -0.25926,0.0439 -0.10141,0.003 -0.20822,-0.0113 -0.31432,-0.0453 -0.10432,-0.0334 -0.19468,-0.0821 -0.26958,-0.13711 -0.14429,-0.10601 -0.21046,-0.21512 -0.24075,-0.27444 -0.0295,-0.0578 -0.0294,-0.0756 -0.0257,-0.0583 0.004,0.0189 0.0118,0.0642 0.0165,0.14325 0.006,0.10518 0.0162,0.2113 0.0508,0.31083 0.0346,0.0995 0.0925,0.18902 0.15282,0.27538 0.16999,0.24324 0.37017,0.45185 0.59586,0.62624 0.22036,0.17026 0.45568,0.3007 0.69594,0.39998 0.462,0.19089 0.94262,0.26663 1.38167,0.29646 0.42445,0.0288 0.85065,0.0167 1.22132,0.006 0.37869,-0.0114 0.68213,-0.0209 0.94291,-0.004 0.0467,0.003 0.0936,0.003 0.14028,4.2e-4 0.57657,-0.0338 1.11745,-0.16957 1.62097,-0.3804 0.48998,-0.20516 0.93688,-0.47809 1.3441,-0.78763 0.78662,-0.59793 1.44284,-1.34636 1.99372,-2.04668 0.0545,-0.0693 0.10744,-0.14086 0.14464,-0.22085 0.0372,-0.08 0.0578,-0.16653 0.0757,-0.25292 0.0198,-0.0954 0.0368,-0.16105 0.0498,-0.20346 0.0137,-0.0449 0.0177,-0.0468 0.006,-0.023 -0.007,0.0132 -0.0212,0.0399 -0.0457,0.0745 -0.0243,0.0343 -0.0636,0.0834 -0.12164,0.13596 -0.0588,0.0532 -0.13959,0.11254 -0.24462,0.16095 -0.10698,0.0493 -0.22631,0.0813 -0.35229,0.0902 -0.12441,0.009 -0.23618,-0.006 -0.32925,-0.0313 -0.091,-0.0244 -0.1623,-0.0577 -0.21244,-0.0857 -0.0937,-0.0523 -0.14474,-0.10384 -0.15172,-0.11084 -0.0107,-0.0108 -0.007,-0.009 0.0133,0.0177 0.0193,0.0248 0.0444,0.0593 0.0784,0.10832 0.0656,0.0943 0.152,0.22603 0.25609,0.37388 0.10061,0.1429 0.22806,0.31489 0.37773,0.47923 0.14647,0.16082 0.3442,0.348 0.5963,0.49566 0.12863,0.0753 0.27746,0.14399 0.44582,0.19191 0.10224,0.0291 0.20961,0.05 0.32123,0.0604 1.14387,0.31692 2.30384,0.39331 3.43423,0.3494 1.15472,-0.0448 2.29519,-0.21629 3.36287,-0.3922 0.0639,-0.0105 0.1268,-0.0265 0.18799,-0.0477 0.31377,-0.10875 0.6099,-0.23095 0.88656,-0.33016 0.28507,-0.10222 0.51909,-0.17059 0.71534,-0.19938 0.094,-0.0138 0.16529,-0.0162 0.21763,-0.013 0.051,0.003 0.0779,0.0109 0.0923,0.0164 0.0112,0.004 0.0215,0.01 0.0357,0.0221 0.0154,0.0134 0.0482,0.0465 0.0901,0.11828 0.0198,0.0338 0.0413,0.0666 0.0644,0.0983 0.18358,0.25087 0.39072,0.4683 0.61801,0.65385 0.22703,0.18533 0.46801,0.33382 0.71595,0.45169 0.49341,0.23458 1.00539,0.34372 1.48256,0.39181 0.47606,0.048 0.94835,0.0379 1.37141,0.0147 0.42959,-0.0235 0.82764,-0.0608 1.16844,-0.0803 0.0127,-7.3e-4 0.0254,-0.002 0.0381,-0.003 0.60634,-0.0552 1.08454,-0.11342 1.57262,-0.11244 0.2337,4.6e-4 0.4471,0.0154 0.64569,0.0485 0.1986,0.0331 0.38235,0.0842 0.55589,0.15729 0.0523,0.022 0.10612,0.0401 0.16109,0.0541 0.63825,0.16263 1.28546,0.37806 1.96841,0.61034 0.67946,0.23109 1.3961,0.47953 2.12344,0.68391 0.73874,0.20757 1.51023,0.37628 2.30925,0.4429 0.81251,0.0677 1.6495,0.0296 2.50678,-0.17567 0.0677,-0.0162 0.13385,-0.0386 0.1975,-0.0669 0.12078,-0.0537 0.22428,-0.11686 0.30908,-0.17628 0.0857,-0.0601 0.16195,-0.12309 0.22776,-0.18232 0.13002,-0.11704 0.24491,-0.24262 0.33721,-0.34935 0.0932,-0.10781 0.18293,-0.21938 0.25179,-0.30458 0.0768,-0.095 0.12739,-0.15677 0.16827,-0.2023 0.0177,-0.0197 0.0289,-0.0305 0.0258,-0.0277 -0.003,0.003 -0.0189,0.0201 -0.0729,0.0556 -0.0258,0.017 -0.0657,0.041 -0.11862,0.065 -0.0527,0.0239 -0.12829,0.0522 -0.22353,0.0702 -0.0972,0.0184 -0.21829,0.0266 -0.35415,0.006 -0.13893,-0.0214 -0.27255,-0.0703 -0.39246,-0.14371 -0.11786,-0.0721 -0.2051,-0.15704 -0.26716,-0.23397 -0.0611,-0.0757 -0.0999,-0.14613 -0.12385,-0.19749 -0.0453,-0.0971 -0.0571,-0.16793 -0.0586,-0.1768 -0.003,-0.0187 -1.7e-4,-0.005 0.001,0.0299 0.001,0.0363 0.002,0.0899 -9.9e-4,0.16475 -0.003,0.0756 -0.003,0.15164 0.009,0.22625 0.0123,0.0746 0.0374,0.14641 0.0642,0.21713 0.17632,0.46587 0.46488,0.86981 0.7937,1.18905 0.33821,0.32836 0.7476,0.5954 1.19299,0.76027 0.22902,0.0848 0.47324,0.14461 0.72687,0.16922 0.25802,0.025 0.52638,0.0136 0.79532,-0.0458 0.27443,-0.0606 0.53988,-0.16919 0.78602,-0.32797 0.24991,-0.16122 0.46734,-0.36605 0.65093,-0.60475 0.0457,-0.0594 0.0854,-0.12321 0.1186,-0.19042 0.0359,-0.0727 0.0636,-0.10236 0.073,-0.11149 0.009,-0.008 0.0164,-0.014 0.0319,-0.0209 0.0194,-0.008 0.0595,-0.0219 0.12858,-0.0318 0.0733,-0.0105 0.16695,-0.0159 0.28962,-0.0146 0.24859,0.003 0.58015,0.0365 0.95425,0.0494 0.19322,0.007 0.40373,0.007 0.62136,-0.0113 0.22571,-0.0189 0.46448,-0.0581 0.70745,-0.13394 0.0225,-0.007 0.0448,-0.0148 0.0669,-0.0232 0.0532,-0.0203 0.0979,-0.0374 0.13183,-0.0503 a 1.1399858,1.1399858 90 0 0 -0.8132,-2.13002 c -0.0247,0.009 -0.0551,0.021 -0.0903,0.0345 -0.0476,0.0127 -0.11021,0.024 -0.19329,0.031 -0.097,0.008 -0.21088,0.01 -0.35213,0.005 -0.26693,-0.009 -0.60468,-0.0464 -1.00932,-0.0506 -0.19183,-0.002 -0.41027,0.005 -0.63764,0.0377 -0.22405,0.0322 -0.47085,0.0913 -0.72049,0.20088 -0.24821,0.10896 -0.48932,0.26359 -0.70751,0.4764 -0.17713,0.17277 -0.32731,0.37231 -0.45224,0.5953 -0.0147,0.014 -0.0264,0.0225 -0.0343,0.0276 -0.0142,0.009 -0.0269,0.0143 -0.0419,0.0176 -0.0168,0.004 -0.0427,0.007 -0.0833,0.003 -0.0404,-0.004 -0.0929,-0.0149 -0.15557,-0.0381 -0.12623,-0.0467 -0.2687,-0.13405 -0.39627,-0.25791 -0.0721,-0.07 -0.13027,-0.14276 -0.17452,-0.21274 -3.3e-4,-0.0117 -7.1e-4,-0.0233 -0.001,-0.0348 -0.004,-0.10269 -0.0127,-0.2137 -0.0317,-0.32549 -0.0179,-0.1053 -0.0514,-0.25191 -0.12337,-0.40612 -0.0373,-0.0798 -0.0906,-0.17406 -0.16736,-0.26924 -0.0777,-0.0964 -0.18181,-0.19639 -0.31765,-0.27948 -0.13785,-0.0843 -0.29052,-0.14015 -0.44959,-0.1647 -0.15595,-0.0241 -0.29821,-0.0152 -0.41759,0.007 -0.11736,0.0222 -0.21607,0.0582 -0.29292,0.093 -0.077,0.0349 -0.14191,0.073 -0.19365,0.10703 -0.10031,0.066 -0.18109,0.13639 -0.23856,0.19058 -0.0596,0.0562 -0.11312,0.11307 -0.15829,0.16339 -0.0872,0.0971 -0.17486,0.20561 -0.24479,0.29212 -0.0761,0.0941 -0.13985,0.17323 -0.20311,0.24637 -0.0632,0.0731 -0.10816,0.11929 -0.13808,0.14622 -0.0127,0.0114 -0.0185,0.0151 -0.0108,0.01 0.006,-0.004 0.0306,-0.021 0.0734,-0.0401 0.0636,-0.0283 0.12976,-0.0507 0.19749,-0.0669 -0.58691,0.14053 -1.17712,0.17169 -1.78641,0.12089 -0.60624,-0.0505 -1.22695,-0.18174 -1.88194,-0.36579 -0.65453,-0.18391 -1.30394,-0.40868 -2.00607,-0.64748 -0.65534,-0.22289 -1.35302,-0.45665 -2.0616,-0.64109 -0.32935,-0.13105 -0.65905,-0.21715 -0.98373,-0.27117 -0.34833,-0.058 -0.68929,-0.0787 -1.01534,-0.0794 -0.61917,-0.001 -1.2528,0.0731 -1.76528,0.12012 -0.3927,0.0229 -0.77795,0.0589 -1.14308,0.0788 -0.37577,0.0206 -0.71335,0.0241 -1.01818,-0.007 -0.30284,-0.0305 -0.54221,-0.0921 -0.73226,-0.18245 -0.0937,-0.0445 -0.17734,-0.097 -0.25307,-0.15878 -0.0661,-0.054 -0.13091,-0.11895 -0.19339,-0.19903 -0.14486,-0.23506 -0.31784,-0.44492 -0.52155,-0.62275 -0.22314,-0.19479 -0.46924,-0.33895 -0.72861,-0.43704 -0.25747,-0.0974 -0.51443,-0.14434 -0.75787,-0.15942 -0.24234,-0.015 -0.47511,0.001 -0.6895,0.0327 -0.42182,0.0619 -0.82437,0.19083 -1.15405,0.30905 -0.29786,0.10681 -0.5646,0.21397 -0.77584,0.29083 -1.02249,0.16729 -2.01001,0.30943 -2.98049,0.34713 -1.01119,0.0393 -1.95682,-0.0378 -2.83903,-0.2975 -0.11765,-0.0346 -0.24019,-0.0501 -0.36276,-0.0457 0.0601,-0.002 0.11452,0.006 0.15903,0.0188 0.0429,0.0122 0.0704,0.0266 0.0823,0.0336 0.0239,0.014 -0.0106,-0.006 -0.0629,-0.0635 -0.0563,-0.0618 -0.12076,-0.14528 -0.19912,-0.25657 -0.0761,-0.10808 -0.15712,-0.23154 -0.24808,-0.36243 -0.0446,-0.0642 -0.0953,-0.13526 -0.14943,-0.20498 -0.0532,-0.0685 -0.12054,-0.15 -0.2,-0.2297 -0.0759,-0.0762 -0.19355,-0.182 -0.35172,-0.27028 -0.0825,-0.046 -0.18557,-0.0927 -0.30783,-0.12553 -0.1244,-0.0334 -0.26699,-0.0518 -0.42175,-0.041 -0.15638,0.011 -0.30563,0.0507 -0.44208,0.11358 -0.13367,0.0616 -0.2444,0.14084 -0.33183,0.22007 -0.0867,0.0785 -0.15424,0.16007 -0.20642,0.23357 -0.0524,0.0738 -0.0944,0.14676 -0.12825,0.21336 -0.0665,0.13092 -0.11541,0.26549 -0.15326,0.3895 -0.0127,0.0415 -0.0247,0.084 -0.0363,0.12738 -0.45713,0.56477 -0.92452,1.0654 -1.42659,1.44704 -0.28273,0.21491 -0.56364,0.3819 -0.84497,0.4997 -0.26666,0.11165 -0.53626,0.18026 -0.81421,0.20318 -0.36893,-0.0186 -0.7592,-0.005 -1.07817,0.005 -0.38258,0.0115 -0.70132,0.0188 -0.99798,-0.001 -0.30315,-0.0206 -0.5152,-0.0668 -0.66554,-0.12891 -0.0737,-0.0305 -0.12917,-0.0634 -0.17261,-0.097 -0.0435,-0.0336 -0.0834,-0.0743 -0.12102,-0.12811 l 0.20361,0.58621 c -0.01,-0.16971 -0.0302,-0.33494 -0.0642,-0.49218 -0.0343,-0.15846 -0.0872,-0.32965 -0.17215,-0.49606 -0.0866,-0.1695 -0.22367,-0.36718 -0.4399,-0.52604 -0.112,-0.0823 -0.24088,-0.15066 -0.38477,-0.19675 -0.14625,-0.0469 -0.29432,-0.0663 -0.43773,-0.0627 -0.14355,0.004 -0.27521,0.0301 -0.38924,0.0672 -0.11513,0.0374 -0.21517,0.0863 -0.29948,0.13668 -0.16915,0.10103 -0.30096,0.22347 -0.39899,0.3316 -0.20512,0.22625 -0.35658,0.49443 -0.46677,0.74014 -0.003,0.006 -0.005,0.0114 -0.008,0.0172 -0.0862,0.20106 -0.19994,0.35781 -0.32434,0.48309 -0.009,0.009 -0.0179,0.0178 -0.027,0.0265 -0.12961,0.12441 -0.28335,0.2299 -0.45987,0.31659 -0.40175,0.19731 -0.8973,0.28412 -1.39772,0.26457 -0.0279,-0.001 -0.0558,-0.001 -0.0837,-1.9e-4 -1.61967,0.0557 -3.03485,0.10497 -4.47262,0.0528 -1.57211,-0.0571 -2.95838,-0.23263 -4.24542,-0.57546 -0.0104,-0.003 -0.0208,-0.005 -0.0313,-0.008 -0.30077,-0.0711 -0.59316,-0.18411 -0.85433,-0.32355 -0.29077,-0.15525 -0.52776,-0.33471 -0.70872,-0.51659 -0.20886,-0.20992 -0.33647,-0.4155 -0.41068,-0.5991 -0.0927,-0.22942 -0.11223,-0.44844 -0.0907,-0.65558 a 1.1399858,1.1399858 90 0 0 -2.26776,-0.23572 z"
       id="path-1-55"
       style="opacity:1;fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:2.1052;stroke-dasharray:none;stroke-opacity:1" />
    <path
       d="m 38.54574,317.63168 c -0.195998,0.72453 -0.422798,1.98254 -0.157764,3.35464 0.102556,0.53094 0.285916,1.10956 0.601679,1.66981 0.284534,0.50484 0.682399,1.00293 1.225263,1.42326 0.0037,0.003 0.0075,0.006 0.01128,0.009 0.889806,0.6714 1.968184,1.1291 3.170294,1.34007 1.0627,0.18649 2.210518,0.17669 3.342045,-0.0453 0.0042,-8.2e-4 0.0084,-0.002 0.01263,-0.003 1.125777,-0.23409 2.186763,-0.81477 3.037866,-1.65894 0.08176,-0.0811 0.161587,-0.16464 0.239328,-0.25056 0.626217,-0.6921 1.194812,-1.62852 1.447014,-2.75996 0.02043,-0.0916 0.03811,-0.18472 0.03561,-0.27857 -0.0025,-0.0938 -0.0251,-0.18587 -0.05037,-0.27629 0.0051,0.0183 0.0033,0.0207 0.0029,0.005 -3.45e-4,-0.0141 8.14e-4,-0.0344 0.0048,-0.057 0.004,-0.0223 0.0089,-0.0369 0.0107,-0.0413 9.03e-4,-0.002 -0.0017,0.0115 -0.03465,0.0545 -0.02652,0.0346 -0.100438,0.12106 -0.240152,0.19092 -0.07146,0.0357 -0.159568,0.0666 -0.261707,0.0811 -0.101955,0.0144 -0.204381,0.0106 -0.301412,-0.01 -0.0947,-0.02 -0.172,-0.0532 -0.230384,-0.0865 -0.05677,-0.0324 -0.09475,-0.0643 -0.115946,-0.0843 -0.03844,-0.0364 -0.03319,-0.0445 0.0012,0.0169 0.05997,0.10705 0.136869,0.20377 0.227655,0.28632 0.29474,0.268 0.623979,0.45244 0.961263,0.57692 0.321058,0.11849 0.643926,0.18076 0.945426,0.21487 0.538115,0.0609 1.150564,0.0384 1.512616,0.0472 0.0182,4.4e-4 0.03641,4.5e-4 0.05461,2e-5 0.721362,-0.017 1.393476,-0.17567 2.017327,-0.43468 0.606573,-0.25184 1.157455,-0.59418 1.660301,-0.97943 0.969188,-0.74255 1.794373,-1.67313 2.509759,-2.47318 0.006,-0.007 0.0119,-0.0135 0.01773,-0.0203 0.04589,-0.0538 0.09686,-0.11449 0.151761,-0.17936 0.05469,-0.0646 0.11225,-0.1322 0.169726,-0.19822 0.05741,-0.066 0.111986,-0.12716 0.160963,-0.17978 0.0507,-0.0545 0.08524,-0.0887 0.104147,-0.10604 0.0092,-0.008 0.0055,-0.004 -0.0091,0.007 -0.0079,0.006 -0.06008,0.0463 -0.145418,0.087 -0.0441,0.021 -0.122772,0.0546 -0.228028,0.0773 -0.102557,0.0221 -0.277807,0.0442 -0.487727,-0.006 -0.107939,-0.0258 -0.220711,-0.0697 -0.32991,-0.13754 -0.109481,-0.068 -0.202138,-0.15164 -0.277132,-0.24371 -0.07392,-0.0907 -0.125051,-0.18261 -0.160206,-0.26485 -0.03482,-0.0815 -0.05505,-0.15591 -0.06712,-0.21667 -0.02326,-0.11706 -0.02179,-0.21165 -0.01865,-0.26444 0.0033,-0.0562 0.01079,-0.0987 0.0155,-0.12214 0.01043,-0.0518 0.01564,-0.0604 0.01276,-0.0523 -0.0057,0.0162 -0.04037,0.10259 -0.102029,0.23078 -0.02534,0.0527 -0.04659,0.10725 -0.06356,0.1632 -0.0705,0.23241 -0.167355,0.50917 -0.265837,0.81728 -0.09589,0.30002 -0.198262,0.64756 -0.265313,1.01212 -0.06676,0.36298 -0.104589,0.77331 -0.05559,1.20356 0.04958,0.43537 0.18716,0.88119 0.456734,1.30629 0.01757,0.0277 0.03634,0.0547 0.05624,0.0808 0.308406,0.40443 0.697917,0.69733 1.126388,0.88407 0.421722,0.18381 0.865128,0.25828 1.290657,0.25417 0.42327,-0.004 0.841038,-0.0858 1.227839,-0.22669 0.369182,-0.13448 0.723453,-0.32773 1.036879,-0.57496 0.548343,-0.3769 1.006476,-0.82087 1.405291,-1.25821 0.394759,-0.43289 0.781543,-0.91796 1.106825,-1.30453 l -1.997087,-0.5487 c 0.09368,0.56869 0.290504,1.12434 0.594402,1.62837 0.302068,0.50098 0.707838,0.9472 1.214134,1.2991 0.866822,0.65131 1.847318,1.01414 2.810929,1.20165 0.982454,0.19117 1.97743,0.20613 2.880968,0.14315 l -0.376734,-0.0367 c -0.09162,-0.0248 -0.177397,-0.0716 -0.246171,-0.13053 -0.06325,-0.0542 -0.09158,-0.10004 -0.09851,-0.11176 -0.007,-0.0118 0.0047,0.008 0.02228,0.0534 0.02033,0.0524 0.03967,0.10986 0.07223,0.20532 0.02928,0.0859 0.06871,0.20066 0.117013,0.31908 0.04928,0.12081 0.11433,0.26211 0.20262,0.4067 0.08979,0.14704 0.206773,0.30276 0.361458,0.4475 0.101593,0.0951 0.214984,0.18118 0.34046,0.25553 0.888716,0.84024 1.941555,1.51236 3.063677,1.95494 1.221184,0.48166 2.533262,0.69548 3.833569,0.56091 0.03762,-0.004 0.07503,-0.01 0.11208,-0.0173 0.290887,-0.0598 0.613237,-0.14372 0.938387,-0.25444 0.332119,-0.11309 0.678867,-0.25806 1.005044,-0.44179 0.332185,-0.18712 0.670491,-0.42981 0.949227,-0.7453 0.144408,-0.16345 0.276257,-0.35036 0.381326,-0.56239 0.107531,-0.217 0.183955,-0.45433 0.218491,-0.7089 l -2.267506,-0.0838 c 0.02274,0.37262 0.104871,0.75093 0.231079,1.10226 0.131763,0.36679 0.320385,0.72911 0.569306,1.04748 0.261411,0.33434 0.603734,0.63801 1.03369,0.83252 0.224301,0.10148 0.465358,0.16981 0.719125,0.19831 0.261415,0.0294 0.523469,0.015 0.780872,-0.0383 0.0072,-0.001 0.01429,-0.003 0.02142,-0.005 0.305236,-0.0693 0.572489,-0.18593 0.800931,-0.32156 0.246006,-0.14606 0.451753,-0.31687 0.620425,-0.48457 0.389252,-0.38702 0.645781,-0.82206 0.80024,-1.13042 A 1.1399858,1.1399858 90 0 0 83.71968,323.2454 c -0.09343,0.18652 -0.219019,0.38535 -0.36925,0.53472 -0.0616,0.0612 -0.121104,0.10782 -0.176846,0.14091 -0.04627,0.0275 -0.08941,0.0454 -0.130955,0.056 -0.02845,0.005 -0.04542,0.004 -0.0539,0.003 -0.0092,-0.001 -0.01951,-0.003 -0.03375,-0.01 -0.02908,-0.0131 -0.09423,-0.0533 -0.177339,-0.15958 -0.07936,-0.10151 -0.158232,-0.24279 -0.219714,-0.41394 -0.05898,-0.16418 -0.09251,-0.33007 -0.101068,-0.47036 -0.02135,-0.34976 -0.05454,-0.71172 -0.229031,-1.01559 -0.08724,-0.15194 -0.207596,-0.28586 -0.354362,-0.38155 -0.146765,-0.0957 -0.319329,-0.15204 -0.494413,-0.15851 -0.175085,-0.006 -0.351338,0.037 -0.504766,0.12158 -0.153428,0.0846 -0.283338,0.20927 -0.381559,0.35435 -0.196442,0.29017 -0.256268,0.64869 -0.303375,0.99592 3.54e-4,-0.003 0.0027,-0.007 -0.0021,0.003 -0.0046,0.009 -0.01734,0.0315 -0.04706,0.0651 -0.06195,0.0701 -0.175227,0.16455 -0.359575,0.26839 -0.175981,0.0991 -0.387925,0.19064 -0.620993,0.27001 -0.205723,0.0701 -0.414406,0.12604 -0.60658,0.16763 -0.879822,0.0811 -1.80871,-0.0656 -2.705972,-0.41951 -0.887227,-0.34994 -1.728567,-0.89579 -2.427893,-1.58125 -0.0496,-0.0486 -0.10057,-0.0963 -0.158161,-0.13512 -0.05759,-0.0388 -0.120928,-0.0682 -0.184602,-0.0959 0.03152,0.0137 0.06266,0.0345 0.08778,0.058 0.02235,0.0209 0.03053,0.0355 0.02659,0.029 -0.0049,-0.008 -0.01753,-0.0309 -0.03737,-0.0796 -0.02044,-0.0501 -0.04095,-0.10817 -0.0702,-0.19392 -0.02546,-0.0747 -0.06281,-0.18635 -0.104279,-0.29334 -0.04223,-0.10897 -0.101611,-0.24781 -0.185615,-0.38988 -0.08594,-0.14533 -0.205635,-0.3091 -0.37987,-0.45851 -0.179203,-0.15368 -0.394887,-0.27262 -0.643085,-0.3397 -0.06132,-0.0166 -0.12323,-0.0319 -0.186446,-0.0381 -0.06321,-0.006 -0.126927,-0.003 -0.190288,0.001 -0.772493,0.0539 -1.557009,0.0353 -2.28693,-0.10669 -0.717715,-0.13966 -1.359522,-0.394 -1.889924,-0.79632 -0.01459,-0.0111 -0.02945,-0.0218 -0.04456,-0.0321 -0.235531,-0.16139 -0.42724,-0.36891 -0.573542,-0.61156 -0.146194,-0.24246 -0.247866,-0.52178 -0.297263,-0.82166 -0.03956,-0.24016 -0.08524,-0.48482 -0.206036,-0.69613 -0.120795,-0.2113 -0.319376,-0.38155 -0.554075,-0.44604 -0.234699,-0.0645 -0.492389,-0.0196 -0.70419,0.10033 -0.211802,0.11993 -0.376074,0.3069 -0.532786,0.49314 -0.38297,0.45511 -0.691964,0.8469 -1.046981,1.23621 -0.342701,0.37581 -0.676431,0.68879 -1.037222,0.93269 -0.02784,0.0188 -0.05483,0.0389 -0.0809,0.0601 -0.115567,0.094 -0.259616,0.17609 -0.41973,0.23442 -0.16058,0.0585 -0.322404,0.0877 -0.469525,0.0891 -0.1473,0.001 -0.26688,-0.0248 -0.357678,-0.0644 -0.07331,-0.0319 -0.137513,-0.0764 -0.194058,-0.13977 -0.04915,-0.09 -0.07805,-0.18634 -0.09091,-0.29923 -0.016,-0.14052 -0.0076,-0.3143 0.03262,-0.53318 0.04077,-0.22167 0.108545,-0.46089 0.194685,-0.73039 0.07752,-0.24253 0.166791,-0.49812 0.250364,-0.76654 0.0635,-0.13578 0.118287,-0.26373 0.159434,-0.38036 0.02442,-0.0692 0.05244,-0.15784 0.07223,-0.25609 0.01012,-0.0503 0.0208,-0.11621 0.02535,-0.19255 0.0043,-0.073 0.005,-0.18445 -0.02104,-0.31535 -0.01345,-0.0677 -0.03553,-0.14828 -0.07267,-0.23516 -0.03747,-0.0877 -0.09138,-0.1842 -0.168523,-0.27891 -0.07822,-0.096 -0.174545,-0.18294 -0.288106,-0.25344 -0.113318,-0.0703 -0.23062,-0.11619 -0.343501,-0.14312 -0.219814,-0.0524 -0.406608,-0.03 -0.522217,-0.005 -0.118348,0.0255 -0.211622,0.0644 -0.271706,0.0931 -0.117392,0.0559 -0.207194,0.12072 -0.257206,0.15889 -0.05684,0.0434 -0.107338,0.0874 -0.148332,0.12499 -0.08205,0.0752 -0.162536,0.15827 -0.232306,0.23322 -0.07233,0.0777 -0.1449,0.15939 -0.211834,0.23628 -0.06773,0.0778 -0.133167,0.15469 -0.190355,0.22225 -0.05372,0.0635 -0.101514,0.12028 -0.13804,0.16323 -0.74037,0.82796 -1.421589,1.58591 -2.187555,2.17276 -0.38458,0.29464 -0.764638,0.52445 -1.147928,0.68358 -0.380764,0.15809 -0.76752,0.24769 -1.172084,0.26036 -0.575793,-0.0129 -0.876504,0.0131 -1.281932,-0.0327 -0.178154,-0.0202 -0.311056,-0.0509 -0.412308,-0.0883 -0.04923,-0.0182 -0.09034,-0.0376 -0.125339,-0.0581 -0.08263,-0.12 -0.177463,-0.23536 -0.287281,-0.33925 -0.09101,-0.0861 -0.197534,-0.16927 -0.321195,-0.23982 -0.126051,-0.0719 -0.269387,-0.13032 -0.428133,-0.16386 -0.161852,-0.0342 -0.327117,-0.0398 -0.489584,-0.0168 -0.163404,0.0231 -0.31045,0.0732 -0.438199,0.13712 -0.254474,0.12724 -0.432375,0.3082 -0.549763,0.46136 -0.123323,0.16089 -0.210707,0.33089 -0.272507,0.4853 -0.06476,0.1618 -0.110007,0.32783 -0.138702,0.48911 -0.02977,0.16737 -0.04361,0.34011 -0.0394,0.51212 0.0016,0.0663 0.006,0.13391 0.01347,0.20234 -0.171495,0.59491 -0.492953,1.1159 -0.859999,1.52156 -0.05009,0.0554 -0.101552,0.10922 -0.154251,0.16149 -0.552333,0.54783 -1.220035,0.90352 -1.890388,1.04422 -0.861772,0.16822 -1.724732,0.17216 -2.502483,0.0357 -0.868599,-0.15243 -1.608804,-0.47661 -2.185238,-0.90998 -0.274471,-0.21376 -0.47765,-0.4664 -0.629471,-0.73577 -0.172088,-0.30534 -0.28348,-0.64194 -0.349314,-0.98276 -0.174735,-0.90462 -0.02633,-1.78579 0.120036,-2.32686 a 1.1399858,1.1399858 90 0 0 -2.200864,-0.59538 z"
       id="path-1-7"
       style="opacity:1;fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:2.1052;stroke-dasharray:none;stroke-opacity:1" />
    <path
       style="opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.1052;stroke-dasharray:none;stroke-opacity:1"
       d="m 914.46763,478.93835 c 0,0 -714.60767,-143.86938 -714.60767,-143.86938"
       id="path48235" />
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="66.962624"
       y="220.39363"
       id="text30644-85-89-5-9"><tspan
         id="tspan30642-905-67-7-2"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="66.962624"
         y="220.39363">X</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="1.2539203"
       y="281.5499"
       id="text2668"><tspan
         id="tspan2666"
         style="stroke-width:0.557"
         x="1.2539203"
         y="281.5499">Observaciones aqui del reporte</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke-width:0.557001"
       x="2.242465"
       y="332.36917"
       id="text9489"><tspan
         id="tspan9487"
         style="stroke-width:0.557"
         x="2.242465"
         y="332.36917">Con la firma de este documento el usuario declara conocer: </tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke-width:0.557001"
       x="2.3419371"
       y="335.06012"
       id="text9493"><tspan
         id="tspan9491"
         style="stroke-width:0.557"
         x="2.3419371"
         y="335.06012">A) La inspección se realiza bajo los parametros de la Res. 40245 Númeral 10.1 y 10.3 de MINMINA.</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke-width:0.557001"
       x="2.1969938"
       y="337.75104"
       id="text9497"><tspan
         id="tspan9495"
         style="stroke-width:0.557"
         x="2.1969938"
         y="337.75104">B) Cualquier modificacion a los tanques estacionarios debe ser informada y automáticamente el certificado pierde validez.</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke-width:0.557001"
       x="2.242465"
       y="340.44199"
       id="text9501"><tspan
         id="tspan9499"
         style="stroke-width:0.557"
         x="2.242465"
         y="340.44199">C) Se puede presentar quejas y/o apelación de los resultados en los primeros 5 diás hábiles a la revisión al email qya@qcsas.com</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke-width:0.557001"
       x="2.2149992"
       y="343.1329"
       id="text9508"><tspan
         id="tspan9506"
         style="stroke-width:0.557"
         x="2.2149992"
         y="343.1329">D) Con la firma del presente documento el titular autoriza a que los Datos Personales sean recolectados y tratados de conformidad con las políticas y procedimiento en materia de protección y tratamiento de datos personales </tspan><tspan
         style="stroke-width:0.557"
         x="2.2149992"
         y="345.55811"
         id="tspan9510">lo cual se puede consultar en nuestra pagina web.</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke-width:0.557001"
       x="2.185626"
       y="347.94055"
       id="text9517"><tspan
         id="tspan9515"
         style="stroke-width:0.557"
         x="2.185626"
         y="347.94055">E) Eventos en los cuales la compañía Q-CHEKER SAS no necesita de la autorización del titular para suministrar los datos personales, Información requerida por una entidad pública como, Ministerios de Minas, Superintendencia de </tspan><tspan
         style="stroke-width:0.557"
         x="2.185626"
         y="350.36575"
         id="tspan9519">Industria y Comercio, Superservicios, Creg, Onac, entre otras.</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="96.255066"
       y="88.490967"
       id="text2073"><tspan
         id="tspan2071"
         style="stroke-width:0.557"
         x="96.255066"
         y="88.490967">observacion</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="6.3772225"
       y="328.31705"
       id="text11729"><tspan
         id="tspan11727"
         style="stroke-width:0.557"
         x="6.3772225"
         y="328.31705">otro elemento</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="112.06937"
       y="324.99954"
       id="text11733"><tspan
         id="tspan11731"
         style="stroke-width:0.557"
         x="112.06937"
         y="324.99954">nombre del firmante</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="111.69566"
       y="328.07468"
       id="text11737"><tspan
         id="tspan11735"
         style="stroke-width:0.557"
         x="111.69566"
         y="328.07468">cedula de firmante</tspan></text>
  </g>
  <metadata
     id="metadata1049">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:creator>
          <cc:Agent>
            <dc:title>Julian Quintero</dc:title>
          </cc:Agent>
        </dc:creator>
        <dc:rights>
          <cc:Agent>
            <dc:title>Julian Quintero</dc:title>
          </cc:Agent>
        </dc:rights>
        <dc:publisher>
          <cc:Agent>
            <dc:title>Julian Quintero</dc:title>
          </cc:Agent>
        </dc:publisher>
        <dc:language>español</dc:language>
        <dc:subject>
          <rdf:Bag>
            <rdf:li>reporte</rdf:li>
          </rdf:Bag>
        </dc:subject>
        <cc:license
           rdf:resource="http://scripts.sil.org/OFL" />
      </cc:Work>
      <cc:License
         rdf:about="http://scripts.sil.org/OFL">
        <cc:permits
           rdf:resource="http://scripts.sil.org/pub/OFL/Reproduction" />
        <cc:permits
           rdf:resource="http://scripts.sil.org/pub/OFL/Distribution" />
        <cc:permits
           rdf:resource="http://scripts.sil.org/pub/OFL/Embedding" />
        <cc:permits
           rdf:resource="http://scripts.sil.org/pub/OFL/DerivativeWorks" />
        <cc:requires
           rdf:resource="http://scripts.sil.org/pub/OFL/Notice" />
        <cc:requires
           rdf:resource="http://scripts.sil.org/pub/OFL/Attribution" />
        <cc:requires
           rdf:resource="http://scripts.sil.org/pub/OFL/ShareAlike" />
        <cc:requires
           rdf:resource="http://scripts.sil.org/pub/OFL/DerivativeRenaming" />
        <cc:requires
           rdf:resource="http://scripts.sil.org/pub/OFL/BundlingWhenSelling" />
      </cc:License>
    </rdf:RDF>
  </metadata>
</svg>
    """
    return svg_code