# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os


def simmodsuite_releases():
    releases = [
    {
    'version': '2023.1-230428dev',
    'components': {
       'msparalleladapt': ['16c886fe9556b90fea99e2b76b9b679cd2f044ac73764939881361009df7776d', 'paralleladapt'],
       'pskrnl': ['e852750446c2ca98d0c8b47d83d8dcd087a2c10b0a6683a878d9eba4c167b59a', 'parasolid'],
       'msadv': ['ccd3e2f69cf1ca637b0fae0ae1dc8d16e73569ad51cf65e667d262a8bcef0e00', 'adv'],
       'gmcore': ['b2dfebf01755437ea20942d91177ced1c5445d8f868d8b8023bfb49682ded11b', 'base'],
       'psint': ['b91d28606182bf1efe286708da43d57d00dd482f06ee8cb0ade3f6e53c73f164', 'parasolid'],
       'mscrack': ['5a70fd3ea9b4dfca91d142c10820d0f8935fa85bfaab5ca14070f1dab470ea13', 'crack'],
       'aciskrnl': ['2f0c328ffde7bea1a735ae2609f9395e70630d8d4eb51bc34934c0d6c3d58753', 'acis'],
       'gmadv': ['007c5422350c48b3b072d68d44dcd4832245565119e3041ffb9ac3d67b4dfd22', 'advmodel'],
       'discrete': ['beec74b4b01c735736a39ad1a7f58b380717eb07bc6aa89287a5ad2679053682', 'discrete'],
       'msparallelmesh': ['5d5db7e62893f2dce8ce85b3601784799654b5cea2f87a05e30563d5f7c55148', 'parallelmesh'],
       'gmvoxel': ['9348c3445ce6cdff39fa801818fe9a320615757981de75dee415aa1197cb231f', 'voxel'],
       'fdcore': ['d3291a9da8e3ee9fb9ac373e4ceca701881d2ada04734718b42fc2074d1b77fb', 'base'],
       'msadapt': ['b5d33b4896a17ed13c9e4961e9f41c55683935eec266aa9545a71574706c2aa3', 'base'],
       'gmabstract': ['3b85b3949f84eab105cb8775f582431f341d0f956c501017213bc2faeb897fd9', 'abstract'],
       'mscore': ['708dbafb07e0bdccc2e820f18e9019eceb49bff39ae729c11bf930f003acadd2', 'base'],
       },
    'docs': {
       'GeomSimAbstract': ['af057e1f2f3e071fe9eacee5fbd48309682bfd04c7b0c879bd8612cbc34e791b', 'abstract'],
       'GeomSimDiscrete': ['52d29bb2820f9643b8c233b0f6c3509acb9532bbab18ce9bcc437fb1a8e987fe', 'discrete'],
       'GeomSim': ['539fea7130c62aaa313cc8414628bb68f66277d7d20c3320d4ed6c3e46bcd398', 'base'],
       'GeomSimParasolid': ['c54888b3bad1604dff6c26091554239a47e268d185169d630c55485a3e62ffde', 'parasolid'],
       'ParallelMeshSim': ['5541a0b50b66adcbb55f2043b54d3d6a346b51876e15dc6cc317589e2b3de505', 'parallelmesh'],
       'ParallelMeshSimAdapt': ['ae4f010223cceb9ff4771e3c333ec81d5a471a1b71dccfbcdedcc526970f429d', 'paralleladapt'],
       'GeomSimAcis': ['567728de91e5cd310e5d6ae4ec3e8fe354a02952ca6f96072ef2f5acd17c435c', 'acis'],
       'GeomSimVoxel': ['8ed2f0ccde70fb4f9e35a74de4d9584ec778eca16ab00f17acf9603c4831572f', 'voxel'],
       'FieldSim': ['420c06fc0867fc7dc5d6c2bdf9eb6abd5116a9c5cb3427286ebd17def1b7ec6d', 'base'],
       'MeshSimAdvanced': ['3c9ff434e6c101dfe712c0943aa6beab8d47fdc6735ab5df4a154453f949e5b7', 'adv'],
       'GeomSimAdvanced': ['ab829df31bb690073a761abc69be3e24172b811b0ba946beef3aa4491e1af2ae', 'advmodel'],
       'GeomSimDiscreteModeling': ['3f620a3df57060d4c063a6f236e709884a3c67dcac763aa797cdbb81b8d14bda', 'discrete'],
       'MeshSimCrack': ['4e1cb0f4d073a7a59998c3099ccb6346ca66746cca3080b734b593c0745266a1', 'crack'],
       'MeshSimAdapt': ['ed3350b849fd7c1a220815b95a4af3c6c822f3efc53e847217da03b9de15256b', 'base'],
       'MeshSim': ['40eee3108c01f299d16c8de8583cbffbed54af2ecf135a8b6fec046b796b4502', 'base'],
       }
    },
    {
        'version': '18.0-220930beta',
        'components': {
           'discrete': ['8d0f15475967e19d0c8d3e07316a9105c18a1cd509b7a86503848ca95372df8c', 'discrete'],
           'gmadv': ['9fb61eebce87020b6cb4934f2c2b42a5c161421062498017053ee84d85c358d4', 'advmodel'],
           'aciskrnl': ['bdc3cc870f716172c8a41bd6fb30b07e66666628b379273a4d722fe93bd87570', 'acis'],
           'msparallelmesh': ['fcad8decb1af2c0c8d8a2503df31589ff83bf7b659ec28fc650312dd7374cf91', 'parallelmesh'],
           'msparalleladapt': ['5a0339defd41358f041a2a899563c7394dedd13f3a435fa0083f357e2d159ba3', 'paralleladapt'],
           'gmcore': ['4ba94be5da5a49e74fce5616cd86389eb5be7205add754837be1920824f11113', 'base'],
           'pskrnl': ['c958315c2ad2c0dd90655ab6a55a7790e0f638eca02c70922f27d73f2a128c31', 'parasolid'],
           'gmvoxel': ['6e1e0d333ca4b4c05aa0ee7837b0a6772e5dc4f451625ba769153c624dfcca0e', 'voxel'],
           'msadapt': ['8ee2a942528d8338242e14b9425c89613fdab38bf3b2a8966bc548038ea7bb81', 'base'],
           'gmabstract': ['6280d0bf496177b5c08a95473241329e0e3637fefa595ff68d053f36c6f4b7ef', 'abstract'],
           'mscore': ['e09bfbb8f8d5c5e2248a72207ab79d90de24d05fd9d093bc458848e5327c4dd6', 'base'],
           'msadv': ['a2aa0b3fea780015eaffc42f72b0daa234dfdf3de9cc5abb661450e24d235754', 'adv'],
           'fdcore': ['0ddd7feb91f3fabe6a6da438616d520b51395a8e8b9e1cf6073e11a3644b89b4', 'base'],
           'psint': ['8d460d12b48d3b2432267fa4182b832b567e252d6e42a937243404fac970ae9f', 'parasolid'],
        },
        'docs': {
           'GeomSim': ['3a00c6a0e37254c8c4e4d94c2ab0eab695a35858a9165c433baf755d265d5af5', 'base'],
           'MeshSimAdapt': ['70bf8c7b6451f9ff0eada8845072250bfdff66c1e6941698c68aa8090fe343b6', 'base'],
           'GeomSimAcis': ['fe6f931581fa1d7489fec7265fbaf7ecb0798836584c7add441cbdb705a69b74', 'acis'],
           'GeomSimAdvanced': ['d504ebb92baf0abb7c0d11b10e975cc90c3d9bd99194801b9654fb3319ea5676', 'advmodel'],
           'MeshSimAdvanced': ['47f790bc94012a2f5c325b7f426f97da0bd12063f8b9f47af1b974702b9564cf', 'adv'],
           'GeomSimAbstract': ['3212083a681cc8517326baecaf8db09fdd2922d2abd9f59769b350901bff1f40', 'abstract'],
           'GeomSimDiscreteModeling': ['de169891a3a81ac83b8536561594f682d04734c50d9488396cc0cf18c65fc39b', 'discrete'],
           'GeomSimDiscrete': ['245b4f00da0542d74c93b21596bcef73991364e886a5035c10f08ae390bca28e', 'discrete'],
           'GeomSimVoxel': ['89689ebf8513e150f697cb44c9fd8d489c4ee2e75c87b90d9985a3ef355757dc', 'voxel'],
           'ParallelMeshSimAdapt': ['47a5d6b5c8e95663d611110e4b6e11404577b4ae6bb2a1403bb0a0b308727b85', 'paralleladapt'],
           'MeshSim': ['5cd6fb69477110b0f63d1b372c3d739b159c7d6d6971e01226eb96cf086735f7', 'base'],
           'GeomSimParasolid': ['55e5a4049adefa54737a52a7ddb60a7c1bf18117362425b8c8258dd408ed2278', 'parasolid'],
           'FieldSim': ['18939b3ca20a48829bb3891f58479a3e36d427251b86d4fc3cf0840802f1f59f', 'base'],
           'ParallelMeshSim': ['4d10a09a5054b1bb554464702826d4486fc27e9453ac015b3107b14e9ca26cdd', 'parallelmesh'],
        }
    },
    {
        'version': '18.0-220913dev',
        'components': {
           'msadapt': ['cab75260d68387117f45e6bdb249a0ebdc52950688d8a049c8dc92f9aca2b0b0', 'base'],
           'fdcore': ['ca26379cd6e1766abc9ac1d561873b1096b0a992b71d46bd6bd16dfa6fa192ac', 'base'],
           'gmvoxel': ['fadb6a62dcde083b8b68685e6e2be85b226915c6f51c1f85419d96ee34ec474b', 'voxel'],
           'mscore': ['a7acd065260000116cbaba2515c9dc19edc55bb28c7dcdf32f01d4411189029b', 'base'],
           'psint': ['25e92f34548aa7e9aabe5501224f2f6cf275739f85f85cdc6afaaa9da11535f6', 'parasolid'],
           'msadv': ['11d9447e72957a4cf30311e44527a117d25814417bae4b8dfdf2bb02925602a5', 'adv'],
           'msparallelmesh': ['713191aec0352f9c4f46fff5bd3b753946a9658082bbe3a349c5af8eda7c9b8f', 'parallelmesh'],
           'gmabstract': ['68ece09f9d233bad9a41084252061628e5d04d10fb07d1ecbf9ae72f33e4b06b', 'abstract'],
           'msparalleladapt': ['9d9e0f54311858e8bb7ba2cd55a6fc4b824f95b4fa39eb2fc41210e90db60c6d', 'paralleladapt'],
           'gmcore': ['66a8e68eb3e301b2222a9b35942396ad889f7d29ba0f9a15fea4b5f95ff95c6e', 'base'],
           'gmadv': ['be6e98f00ee6d89aa0499fa791a94e31cfca14f30ca635ba6d9fd6cc712e4ef2', 'advmodel'],
           'pskrnl': ['447996dede78493dd37a505a2d2cef68658486eee5c695f4c1b2ede02b370ba5', 'parasolid'],
           'discrete': ['4922da9d78d795a52dc79ab1a1d3679fbe26e946ab8079c39dec904121cae22f', 'discrete'],
           'aciskrnl': ['65ad91be12c868582783fcf54bc88c85cdffb7a116688a5b9d1d4763b383407a', 'acis'],
        },
        'docs': {
           'GeomSimParasolid': ['92054cf9ebd1cc99ec2a27afc984252e13584ef852c659ec277f2ac415d5e661', 'parasolid'],
           'GeomSimAcis': ['e7c229b5a23a79ad66d2f86e8a29de706be2c9d4573ebc0c2881d1a2ba912e98', 'acis'],
           'MeshSimAdapt': ['c53565f0fba51b2a8afa5c7b325b8e100906a794321459ce565a3b848050fbb2', 'base'],
           'GeomSim': ['d918ed57176f8f711616c9ed79ff2c0240c41eeea02f700b8990f486901392f9', 'base'],
           'MeshSimAdvanced': ['ba1fd5790e0e312559eee6a8c0952b0b2f98261bd3a0fdc53db5661da24687c3', 'adv'],
           'GeomSimAdvanced': ['1c2f61b38ac657d888e66e4a4f190e5276338d38e0860c86bfcf920c02190da1', 'advmodel'],
           'GeomSimDiscreteModeling': ['f325882084aa33c7e68c8223cfa997e97e776a00beb68b2ac8ed43abde25779a', 'discrete'],
           'ParallelMeshSimAdapt': ['42348bc4331d488e6ea3755085c300794035d9ac088c3091b8a5fc5d7bb7f7e9', 'paralleladapt'],
           'MeshSim': ['277824b6309ee623d32c28ce78352619d72e70a4e12f9756daba1a14ce45b546', 'base'],
           'ParallelMeshSim': ['2d55acbcef154f75b347493a0590aa22e0dbfd47971e735bc458cd0a1f9b850e', 'parallelmesh'],
           'FieldSim': ['23a442068e6191864dd3bb027beb172bfc2f4c234fbd726ac43c77579c84caa9', 'base'],
           'GeomSimVoxel': ['f78725ab8c019ab9cfafaa9293c18d26a43052a0d0be46c9d7aa066b0fa7e64a', 'voxel'],
           'GeomSimDiscrete': ['8a80edea91bfb8e1ce85b5a4cc4c7dbc838c67d6426e4073cd56bfe94dea3fc7', 'discrete'],
           'GeomSimAbstract': ['96b5d0fe9408ce465ae0e2406c7f7c7b0392a51789aa230178952c57bdca5950', 'abstract'],
        }
    },
    {
        'version': '18.0-220822dev',
        'components': {
           'msadv': ['efe8d54358eabaf0e4e7bd5b024268d5eef458fbcacc4fd79988a7b000159308', 'adv'],
           'gmvoxel': ['96856c2656ba94c6780201f96146e3b5ea8e4c25f47677fac33d70c7d1faf866', 'voxel'],
           'psint': ['f04dd5648117c5001cf0ca917ddfa206c6a785ac32f620e901be12e16e8b44b9', 'parasolid'],
           'msadapt': ['da7a9d44671e5d9a9b424340ea77cfc074314c9bdd1a4d3fd86a8f9721689e4f', 'base'],
           'gmcore': ['9cf3b7eb053118f85f3564865ba5cde1fd14e1f1d29bf74bc193115d663c3b70', 'base'],
           'msparallelmesh': ['4e6bd2b19faeaab1701643a98a8faa26b03ba7e195391dec7668946086328651', 'parallelmesh'],
           'pskrnl': ['a5339fa5b764d23be1a49ffb635406f9b1de374e1901715dd1922bef5a62c763', 'parasolid'],
           'gmabstract': ['237ba006ddcc13474b7d85af4ba252c32abb194a58186f2a8f9ae38f1922235b', 'abstract'],
           'gmadv': ['4fc48a8f4a981ef0995568458b0aa2e75186933618fef9fe0c3f1fd3d166e188', 'advmodel'],
           'discrete': ['cfe6b9a47de41aeb201d3a2bb89bf127552788389b7b396d05af4b3c86875dde', 'discrete'],
           'aciskrnl': ['5d7dca9475e96c3d0ef62e868e041a61877e9952f7d2f384e698bd3278578c18', 'acis'],
           'mscore': ['23bcb76ae56bb1012bd15d952356d310ca931c20e030b0c9e4622b655fab1111', 'base'],
           'msparalleladapt': ['36a38ce5bcc2c7e217048e275f1968f2766b4107e4522d3ec7e35d3bf7411e1a', 'paralleladapt'],
           'fdcore': ['d72e57244178e78d3e1214f28a7a77b3cb0313abae62aaf31496e1fc5c5c954a', 'base'],
        },
        'docs': {
           'GeomSimAcis': ['949a2f068130ddbfffb28bdb70646e0e690408c5414ef6604cc68a3a3c19ca16', 'acis'],
           'GeomSimDiscreteModeling': ['0974dd5da58f179569686a3157939c56ceb91119e4c456c53d054d971b80eeaf', 'discrete'],
           'MeshSim': ['9d657a8286b355aea917a42b56410f8b6c590bb870701c4b3945ec9f0cd0400b', 'base'],
           'ParallelMeshSimAdapt': ['fc00ccb3f8fc1b0ccec87f0d5bd985070df57eecc4ff1c4a624f7718e6917c65', 'paralleladapt'],
           'GeomSimParasolid': ['65def0e6677539de3ddbf15b527820b62b5fd524d3071ffd4abd28615b209a52', 'parasolid'],
           'GeomSimAdvanced': ['c8988afa636d35274a6cdd45a8551a225c4dd89a828055890b1bbe7799a19f98', 'advmodel'],
           'MeshSimAdapt': ['1b4953bcb2e6e9f037c38501d65389d3787807ed7db63d37094f1049ba5330c9', 'base'],
           'MeshSimAdvanced': ['981085cf2ce2681744b6642e01f7d4fc8c72d64bc428fb67b7048a9bb9eda31d', 'adv'],
           'FieldSim': ['b70340230a78a11626d3da43fd95a86f07bb957dd4331857eceb9e82e3f2bbc6', 'base'],
           'ParallelMeshSim': ['f4e7d7f76229e17284d52ffdc27923b1581c900d6e7a5b8bb60febbef65571ef', 'parallelmesh'],
           'GeomSimAbstract': ['6464ec899ff71657e3cb9f19f7f3ea7130f884ab68fdfa04082b254e9e53998e', 'abstract'],
           'GeomSimVoxel': ['1b0052aaa1bda382674931e1f496fcfc13aa01e07fe72b75baca28dd3ceb6767', 'voxel'],
           'GeomSimDiscrete': ['35890bbec08dab6a16740880d306efc58cde7d002154d15a0380923ed4cef0c4', 'discrete'],
           'GeomSim': ['ee12d0151f51a4214c092ad6c139dc971dcedfb877e81454eede762f372ea4f1', 'base'],
        }
    },
    {
        'version': '18.0-220810dev',
        'components': {
           'discrete': ['a2ac4c7c9b5571d91b48dd3b2c9f88745268663b75661449fc99e6a34c015a2e', 'discrete'],
           'aciskrnl': ['18170d2757ac2aed4dcbfb4716dae02fce84a7aeda30b7d518e6f6b3ed3a32bf', 'acis'],
           'mscore': ['b13eb832750d42aaee0739253ad1430927dabf58bff50beb7bfea38e1023f94c', 'base'],
           'fdcore': ['29f916e99faebcfa509fefd5a716ab34d0552d44950818718d223a8c575b00fd', 'base'],
           'msadv': ['9bd4bf5fd05f911f67e6220b442626df82ab0bc11571b1575cb6fa03c2c3c816', 'adv'],
           'psint': ['3f06aa5b2b5f495570058f7c442bf991b6c048f055adc945911d2b1586bda782', 'parasolid'],
           'msparalleladapt': ['47cef1c6c55e921d7c384852dd25ab4961e37f94ae0726529412b4e53ecdec06', 'paralleladapt'],
           'msparallelmesh': ['2990386b6a63245f64fdec189576500f676251bffb98bc56370ada88db55cf44', 'parallelmesh'],
           'gmabstract': ['390ba01a801acb811f244baa2b07989cf5c1f6defcdc7cc3f2feb21d0a299146', 'abstract'],
           'gmvoxel': ['b5056aa730b8c3f0654a9ffbc9271010d691ab079d45260703a03c20b50206f5', 'voxel'],
           'gmadv': ['2ab731d5e3c01da0ef16bd3c7e8775dab46f15a2c0403fc6e65442d7533a45e0', 'advmodel'],
           'msadapt': ['88cf477c93f490f23726df560125d4c86f8121e3c7e9e84d70ce501a3a44a932', 'base'],
           'gmcore': ['6d2838a8f34e163aebf7edb80d0e0f2d20bd029be985b9cb826bf90f082eda7e', 'base'],
           'pskrnl': ['743362a97f76f7f83399f15cf2a0819fec1d9a9c0b3d6132446029ff3ecc0e05', 'parasolid'],
        },
        'docs': {
           'GeomSimAbstract': ['3314c16e552d3976dd62aee12fcca19fcd9ab3d52163da0ddc9b7e42f25b764b', 'abstract'],
           'GeomSim': ['8d8223f89376dcdce9144c524202396504dde631024421cd89e81e50c4498060', 'base'],
           'GeomSimDiscrete': ['2c3ed4a36aa26bbcdefe3fc6454f76b446da3e35353935dad6cd2aed54f55701', 'discrete'],
           'GeomSimVoxel': ['dfcc4e5e5851297c4ddd5bf7ebf6e4854c622265ca37c54407ca7a0aebb070f0', 'voxel'],
           'ParallelMeshSim': ['7bd1e123f1ed2700d5faf73f723b3ba9882de2caa11e7be64c2ed6c9f1fad6b1', 'parallelmesh'],
           'ParallelMeshSimAdapt': ['99f6c239022c6dc8c846c7f0d15f9ef75edafef496a4f3296c651c0bfa214d83', 'paralleladapt'],
           'MeshSimAdvanced': ['8b98892eece630d984249dbbdb14c4619172520468186828225bb7ff663df057', 'adv'],
           'MeshSimAdapt': ['ca05fe73a68a32d363bc9e7201354457c426a76fe4353aa1ef1f58e5811ba2ab', 'base'],
           'GeomSimAcis': ['1fa3cd402652e1a8d048171ac29ceabdd7f14d97d8bd21422b5af8f80f94a60e', 'acis'],
           'GeomSimAdvanced': ['feea94de2fb69c740360f6be04cc6ee080a9c57c73574f8765f4abff5945deca', 'advmodel'],
           'GeomSimDiscreteModeling': ['a11acfbd30032f3c4832de61b20ca216dc2595ecb0337e24f69e8fbbcdad4dd0', 'discrete'],
           'FieldSim': ['ab6973296774075997f3978441f8af8614b2fbe933c1bca1f3eb28c529be85d2', 'base'],
           'MeshSim': ['679874516bea1b574d8573ede84dd7d1a2790d639b52a07fc11d98416aeaeb52', 'base'],
           'GeomSimParasolid': ['d4ca60b9a0648b4e0b8215c9f07c61939ca3558680dc752e59affa55c4f1d2af', 'parasolid'],
        }
    },
    {
        'version': '18.0-220720dev',
        'components': {
           'pskrnl': ['ca3f7fcc8b1bf7e8cd2feac84de4939cd30c3936699b70cdb2d6de5b6e8dfddd', 'parasolid'],
           'gmcore': ['c66c5fbd68d498b6c60a7f8cf6c75f2a6a759730b0e63f759e8bc251324b228a', 'base'],
           'gmabstract': ['87e805f9a41c0f04469d4cd61becf5fac1aea7e679bf17785839ededeb7320b9', 'abstract'],
           'gmadv': ['7b2d4726c624fa9b760ce247606723ca771b5b49aa00c8ca60232ffaeca3af6a', 'advmodel'],
           'aciskrnl': ['dc5233ef2bcbc1708122832926232689aca642258607102703684c674f851a9f', 'acis'],
           'discrete': ['aa43aa4252eb51459cb0e3928ac502e5510926e2b136ada5c0c2d4cdad3269c7', 'discrete'],
           'msparalleladapt': ['59fc4c0f87099f3bc7ad59dcb20d87583c72000e0aadd2ad935d961b1c19672d', 'paralleladapt'],
           'fdcore': ['4715614fc4eec6ff7cf59d25b2f3a9f2d3635b0fce371cdb4f581e1840bfa55c', 'base'],
           'mscore': ['0cfccf6f0ab1848bade29e3dec2e6a1cd45cb9baaf5ba9d596bf95809dcd36c7', 'base'],
           'gmvoxel': ['b9aa1c7c9348cdace0660757982334c682c86c51c628104bd9fe6bfda53367bc', 'voxel'],
           'msparallelmesh': ['f6743cd070d210fd1be851c532db5e938c363f9c48de9401ad1a4a23a7f841ef', 'parallelmesh'],
           'msadv': ['faedc693d7ea69006bf58624b30072aabfde6c84ec007d8560d039e963c69143', 'adv'],
           'psint': ['7a7871ee93fe0535d3cce8c544bca04503ba9a2a1ffcc7bfd6b5595728d079f5', 'parasolid'],
           'msadapt': ['ddd58b5023afb63ad33af1a5ecaec5ac6af084d340bf0c2d5d6f250c6c4100f2', 'base'],
        },
        'docs': {
           'GeomSimAbstract': ['5e7908935754eec198a7dc88ff7fa70d37ed91d41bf46e45a22abd6604f7950a', 'abstract'],
           'GeomSimDiscrete': ['5bb974837bf8a4daf569f43870eddf5f785eaa17996c802a0ee9864b20ba5036', 'discrete'],
           'FieldSim': ['48f05c6d2beb92a6c38a63aeb1567f0e869c44ad8dac69d07ad652dd9f6958be', 'base'],
           'GeomSimDiscreteModeling': ['f41a5190d024fbcc99b006a0acb19362f13bd55c658fb00391a153eb7924026b', 'discrete'],
           'MeshSim': ['bc57cc5697504946ce07155f418b83044b87fe63be90a14719456e434dd08258', 'base'],
           'GeomSimVoxel': ['976cc5bb3e141e89de797b2da00f77331e9724869f00529f130191ea2edd6791', 'voxel'],
           'ParallelMeshSim': ['770c8bad5653bcc43db7f5c9d15bd2f13116ed09596338cfc35acf5e6a606a3f', 'parallelmesh'],
           'GeomSim': ['9841052d757675231c7714d01eaf4563273af9a97f822909fbb1f3b2342750fa', 'base'],
           'GeomSimAdvanced': ['ef9211ab6cfaa3a8b21b30d8c1e7e15ef6aea64f0dcd128be6ba36285ba92b93', 'advmodel'],
           'GeomSimParasolid': ['bf980ff0514bbfabe2ab65aa458e3ae34a68adc42ed6b17d0c1faa7101e5c02a', 'parasolid'],
           'MeshSimAdvanced': ['1a86baf34841c6e76851a05328a552cb559cba9110b15951cd484c698de0eda9', 'adv'],
           'MeshSimAdapt': ['1fccf2ce029b2d38968508be318f7055aed4a1f71d523573709e1c4e9350df17', 'base'],
           'GeomSimAcis': ['54197cecb4a79c4e3d2f5ead9b78a837b94f979156e3f86d6a051bf762d8ebfe', 'acis'],
           'ParallelMeshSimAdapt': ['0bc713f9e140ac646db66808d9eb7bea6b112c6d2d8a6b15b70f5e3dc940b455', 'paralleladapt'],
        }
    },
    {
        'version': '18.0-220605dev',
        'components': {
           'gmabstract': ['b406a918652a6da831fea9c38026333e5b4c69779f27aa7a3fde18be7855ea1b', 'abstract'],
           'psint': ['0942b91b09e88f57f8d694cbffbc432a7934287a9ba74c18a9119addb77b31d5', 'parasolid'],
           'msadv': ['e5d50d48cc1666ebd55facd1083746447ed4db5e658f251129138a24855a1865', 'adv'],
           'discrete': ['030c6722d3d974d065fd3235211cd843c9417bfe5283b11b5900cbeffb561b46', 'discrete'],
           'aciskrnl': ['9096361d7d42f713a42c9bae6de70ced4a45d50ed1db21648bfc15b67d861de2', 'acis'],
           'fdcore': ['84f882d709a6a48e7fcac1c5c40c3d339e942b0cd84395edc73959f76a3e8a08', 'base'],
           'msadapt': ['f4062eaa0aa9d1b78d67dfb5a51bdd9de0a15b4337782817fc92d134f5ce48b1', 'base'],
           'mscore': ['7a8ed78f29b543ef434472d71c845b39041835672ae08adb01b1f0f8539af24c', 'base'],
           'gmvoxel': ['a2dec36d6a053ec4b175a5de524550c8fe86798751c1430d42b6b7dc82eb4aca', 'voxel'],
           'msparallelmesh': ['c45a40217535c547d1b0f9116fc7e0ee19f4d04faa034c2b03f3689a9a227d84', 'parallelmesh'],
           'pskrnl': ['289608ebc0ace56221b23f51fcd08eacc453199c33d4712a18c1a6942637439c', 'parasolid'],
           'gmcore': ['fd67888d908e9c9bb7f0a5ec9445dd6791ede0042992da73f4e4ca58035a7d63', 'base'],
           'msparalleladapt': ['1624b0e98966cbe2392c0f48c7e39b579ec9e2e1af6c84ba990470121b4066fd', 'paralleladapt'],
           'gmadv': ['4ea68867447014a27e28d5be9bd42db86d6a408197ac7348e2f104bff3fc61ad', 'advmodel'],
        },
        'docs': {
           'GeomSimAdvanced': ['264a6134b6f581756695457a771a7fd7930950b1e6f351e4dc1605b1fe8d4106', 'advmodel'],
           'MeshSimAdvanced': ['82d696e46d524182334718bc68771ef9c1e792dc408497ca1526ccf317e727d1', 'adv'],
           'GeomSimDiscreteModeling': ['6261c7fe197b15c3693a3211e199564cb76309b54885cd0382874b57a6c55cc6', 'discrete'],
           'MeshSim': ['0db0f025521e18cf5829193169ac3b704291449909240e71eb41fe7fb2e7e977', 'base'],
           'GeomSimVoxel': ['282b8067799781eaebdc95c9e6a8ec575afc8bfd854bdb09c9c30c877b07f831', 'voxel'],
           'ParallelMeshSimAdapt': ['6335269aa1212201dee1fd7732061910db16a2289321f7fb20961d6aa9b11731', 'paralleladapt'],
           'FieldSim': ['f331672d6fea3027a04f30f2669af5c73bec6c6bcbebebc1696bd65791e02ddb', 'base'],
           'GeomSimDiscrete': ['792e0bceed2981b5fd7a521924709d62ca0377034afc716b4f6e65ef53b290af', 'discrete'],
           'GeomSimAbstract': ['ae46a7fdbfb43cc99fc07f07956a5a4b34e4f025491ab66b2db1c5875af78b82', 'abstract'],
           'GeomSim': ['574ebc91e7277e81b5dfe847435861483c985915212bc2bdc68262d41e5e5ed9', 'base'],
           'GeomSimParasolid': ['aa5e36c2946028a2a30e2deb17bc2e00de50bb49b29cd340ca654a3443bbfa0d', 'parasolid'],
           'MeshSimAdapt': ['4579bc0a64fa989484644570f0a21c4e675b73e3614053737639975d39b547ce', 'base'],
           'GeomSimAcis': ['006676bdb218166e41b1306d6b1ef21ba97345e4ba6a18d08cedbc8b4c99d5f8', 'acis'],
           'ParallelMeshSim': ['02bbe53935c0866e22238889b526d38e6040982ad9f28077cedcb95012041f8f', 'parallelmesh'],
        }
    },
    {
        'version': '17.0-220516',
        'components': {
           'aciskrnl': ['00b5f37a900d68d733a15432aecceeeb9bf9544b15cd1bbf4fd9f6be965e528d', 'acis'],
           'discrete': ['8e0f31c82e4c1a5185c2e0bdb0946d5ff010a31098747da1fa379dda4b33daff', 'discrete'],
           'mscore': ['147aecfce5db5ccc9f0d4e760a47a6f5474399798dd02673705fcabd7e9da796', 'base'],
           'fdcore': ['f8f5f9f8c3bbbaff688ae581f62f624151d1f1bc8774e9715dc17860fd2ddaa6', 'base'],
           'gmadv': ['2b8a473007fd7824de26e545cba9fdda92eac65932a08591dc6a0e17157b20e1', 'advmodel'],
           'msparallelmesh': ['b2c08710ff857d8f7abaa29cfea9075abb112058ef45fdd62fcea2a8827b2a60', 'parallelmesh'],
           'msparalleladapt': ['12f8ad71951b6436d01071c9463e936808c020062cd9d5ad22ef2a9e3591cb31', 'paralleladapt'],
           'gmabstract': ['094c0603038459488dc76c7f2983f192d9b81fd1d50ea890b7d687329354afe4', 'abstract'],
           'pskrnl': ['41c4fa6e1969b9c45ed343f513f725b9a5be924630156b51e42d7dd7dc628e5a', 'parasolid'],
           'gmcore': ['1f34db2357791f51240815db40c56459de4f4d88b7efee96b2a5fa72e75a0401', 'base'],
           'msadapt': ['354dd7f7edfa1cd3a736293cf27f7e99a3584ef1e49651e0e21a7a6cdfe41b76', 'base'],
           'gmvoxel': ['26a67c51f8df9385faa2ed7ee71277f14922c91943d7011b98dcf4443cf12c0d', 'voxel'],
           'psint': ['73aef640c04c825f13c17a3f9dd53cae166f5b5c59c6a45eb39f4b9ddfe11b60', 'parasolid'],
           'msadv': ['747e415e2fe975bdb06dbbcedd9084ec236c08e7a3b72fdeb26d29c9502d90d5', 'adv'],
        },
        'docs': {
           'GeomSimVoxel': ['41bf8bfe31e098932857579c3604dcefb5d2b4240f65387e9a513ef611747201', 'voxel'],
           'ParallelMeshSim': ['0b115c5ca2dbcb84dd5bbe03dfb947b105fe450f033bf6ad7c668ef711a3dfbf', 'parallelmesh'],
           'ParallelMeshSimAdapt': ['d303648f1e95a71c54e247d3d379f2d503f55e5478081c4093cdcd3b71836653', 'paralleladapt'],
           'GeomSimDiscrete': ['f342c3e511f5083c79208f0d4b3f7607624605210854b10cd60d0e3619048247', 'discrete'],
           'GeomSim': ['fdec91b4fdd6257a854769bd31d8884ba395e4b968722a48c3b62c8b38bcc05d', 'base'],
           'GeomSimAcis': ['5659b0e5ffd109331718a8992251cf148529fdf26192f08c89f9dff6d6f68a8d', 'acis'],
           'GeomSimAbstract': ['df1424cec61f640bfc2358633a2a832cc0542979eb1c84866a252669b83d6dd6', 'abstract'],
           'MeshSim': ['cb54a874104a49179e9feb9d2ebde31c29286db1b97768b2afc7c2b7be4e841b', 'base'],
           'MeshSimAdapt': ['b6032d5ef2f02fb099efb0caef6e1bb8d9b7dde51f71ff598bb0fe1f46e17a0a', 'base'],
           'FieldSim': ['d66bd23b1b40c4ec1b7b02bdee07ae75b567022026c766b613826ee538fd571c', 'base'],
           'GeomSimDiscreteModeling': ['9c0dd2bae889d10b21a82c2f50f8b987ed0a7d2f1cc83b9096e2b9adeecc1615', 'discrete'],
           'GeomSimParasolid': ['444d13a83f5de28e5979013c110157267e577b459990e391459f010156443ed1', 'parasolid'],
           'GeomSimAdvanced': ['5dac45934be4e29ffdbdcc453a6f1adb5e98f3eac689bd4afeea1ea85f35068b', 'advmodel'],
           'MeshSimAdvanced': ['bc9614f1578ae5391d74c54cb1f20a512a07b30d33edb5c8ea3288095624d4aa', 'adv'],
        }
    },
    {
	'version': '17.0-220511',
	'components': {
	   'msadv': ['f70f7fc4965322bc469095b803a774e8c378bba0543894a41c3277b4a95db074', 'adv'],
	   'psint': ['a55f03b32829a28cffc316b563d0b9fb0fb736dfeb2db82476f38eb02614252a', 'parasolid'],
	   'fdcore': ['2ee0ca378bc1b533700a4bcaf6cb0981e6f45467a6378c3c36d8c509a7dbf06d', 'base'],
	   'msadapt': ['bc506ae42501feec83c4297ee0e7b6de3967ee7697e563559985fe5285d3e0d1', 'base'],
	   'mscore': ['f28225304e86b23bff6a2a18ae8c2c71b5a03b56d44d5622bda17c878d5303dd', 'base'],
	   'gmabstract': ['7a73888b06c2d94efb9da2fef617d7f8495d4706252d666e5792bff362d1609c', 'abstract'],
	   'gmvoxel': ['7f5ace16a62090696f77b3c39dff1c1f7c20e9b9708fc5f222552f766786fe02', 'voxel'],
	   'msparalleladapt': ['2170c4d0f5754b78a60febee8f4ae818c09d318c10f410f3343533407576c937', 'paralleladapt'],
	   'msparallelmesh': ['cc9dc0cb210946b620c23b3f7a10988b69d669946d48905e0029d7de62834e0c', 'parallelmesh'],
	   'gmadv': ['9ff4f58e94c1d50a837d0ebf617477b2393e446c79d621b50ee51a40464d0b2d', 'advmodel'],
	   'gmcore': ['91dbf7bf74002f678306168561fe42e2729e71436994a652bb4e1ea5bbf8037f', 'base'],
	   'pskrnl': ['faffa15a625e9cf8d3ac8c1f82147a74c8b565d61237399578a1f675b44ad5e3', 'parasolid'],
	   'aciskrnl': ['4d08362fdbfe90499690976a88bbee1f3880e59204f851f085efde5164ea719a', 'acis'],
	   'discrete': ['ff4e24f0e6574b8fad1b3bbfc00426143b4159173c97fb67976728954d48545c', 'discrete'],
	},
	'docs': {
	   'GeomSimParasolid': ['025f157e3fbf0b1391b90bc83cc859fd861e93324991d9e09f191c0ea2080000', 'parasolid'],
	   'MeshSimAdapt': ['65a3c17f18a0ac85a8e3d895a6e679c3b268c6f515cab9ddcd21b79b8ec9e413', 'base'],
	   'GeomSimAdvanced': ['7604dda8d96f22024372055e5c31eb12967b36a1a00410320f0ac88aa5fea9ab', 'advmodel'],
	   'MeshSimAdvanced': ['9b70ea43fcdcc01c42ee92651f1204d208b270a36d1f9fbe12d5a1403bce7b8c', 'adv'],
	   'GeomSim': ['73a51bece3cf877cd509214d87cfb68c6890597eac0d759cad2ab133f024766d', 'base'],
	   'GeomSimVoxel': ['872c352dd35e39ffb00861843cdc5ee51866c2045e914815bdfc37b0a71e9c4c', 'voxel'],
	   'FieldSim': ['fac5c9ea6796428a735233ab385114bc60ee01b0413989ece79b69289ca84b0f', 'base'],
	   'ParallelMeshSimAdapt': ['69e89984b951038b94b3d3a029b2592255fe618523b821a26f46656b28f0a650', 'paralleladapt'],
	   'ParallelMeshSim': ['bd62c8ce368c1bebbdb0bfaaa463cf617f5002ede87b34df8cc23bc95176a64d', 'parallelmesh'],
	   'GeomSimAcis': ['29b9fc67e634beab5e9b7f045d57a57e026e0d75defbe9a440ca3b7bc1f22892', 'acis'],
	   'GeomSimDiscreteModeling': ['cd1db1be2f80c22051aea5ccd134ccf2ff1a8e77fb60f17f5538b774d18b7ec5', 'discrete'],
	   'MeshSim': ['1eaf46aa3f829f24aca9b49d05d0202bcee4414339f6d5e4b7fb7de2d39b8612', 'base'],
	   'GeomSimDiscrete': ['a14703942f090824413cee23d38c8c46bbca1d1f5c167a1e21e313cf00051c2d', 'discrete'],
	   'GeomSimAbstract': ['852baeba0c7c9ccc5bed0a845f5163b7e54d2e256f462e083c6c93a1f6f1e1d8', 'abstract'],
	}
    },
    {
        'version': '17.0-220411dev',
        'components': {
           'gmadv': ['b88422a4f9a2d53e2dd02edfe1f2b56a7b37d14ef68ed04363db447e719115ae', 'advmodel'],
           'msparalleladapt': ['c22b4c5d98af21740fe503b9986f5eb1b36f1ba76a1bafc7604420ca5619efed', 'paralleladapt'],
           'gmcore': ['d389b32286b051c32368397e329e22a677648dad47dc32cf4948a0a03fc81073', 'base'],
           'pskrnl': ['9f847c80654ab23647118aaf865d3f9c7cf38997650e482cee7b4f51af2cc922', 'parasolid'],
           'fdcore': ['1b6d90f023d61c8ab175e81913bb74600be2dcabedf6d101daea770ac8af0c1e', 'base'],
           'mscore': ['eb56882d68ba8a53cd6016f30e2f734f59f0287ba7fbf4436e060b0327528b75', 'base'],
           'msadv': ['6d4246ed9ac5d6b218d72e271819933a6b4ee785dbd69eebc19c2919cf966b47', 'adv'],
           'psint': ['165b9b24840702a238f51734cc3aee735ddf3673538a1255735861020b8d03c6', 'parasolid'],
           'discrete': ['454c975e7e76c6c9f2c4fa39f02d912ef407846d42563c5a66b32c2ce2133f8d', 'discrete'],
           'msadapt': ['39bf1973c86f7f912182cc96161d9c42839d7c280ecbcf3f72130abab76e6b73', 'base'],
           'gmabstract': ['43bd8989f9f7cf68790a008c012806bbab551a8e62ce9d3febc6509686ef5a6a', 'abstract'],
           'aciskrnl': ['e7983b5c61dcc85d52917259435933c425b35f64755951a6d8512464c48312f6', 'acis'],
           'msparallelmesh': ['bd01e361a2c5a15790dbf9cb4e876d0f4300c1caad488a440d0a41d679315b79', 'parallelmesh'],
           'gmvoxel': ['cf52b9e2a5cc8ba1b9025e27d639ba4ffb1950a3e3cb7ff0a6b42e078146879d', 'voxel'],
        },
        'docs': {
           'GeomSim': ['46580520affa9676e5938852d4e59deadc5586241b07f15b54b5a1776c4e38eb', 'base'],
           'GeomSimDiscrete': ['52de6096afe613401ebe4e32e3702c4400e1d91cb38c4ad19f0bae14aa50fec9', 'discrete'],
           'ParallelMeshSimAdapt': ['3b6935f41459f13266705b99fafe88d0265e1ba3dc05b299007ee2adeb13180e', 'paralleladapt'],
           'FieldSim': ['96c90bb641613dc0167324e864c688e0595d81489a629964840d3061dd9a79ba', 'base'],
           'GeomSimParasolid': ['f0b5bdbad57cf58d6159ab2da4f08bab3f2b4ac69b09a061ed0e661a21855af2', 'parasolid'],
           'GeomSimAcis': ['6f15ba60a1aa77045711cfba2ea020d0b7ee5bc52fff55f8833aee5a73c274da', 'acis'],
           'GeomSimAbstract': ['159ab0d5b49765fb2dfa659333957fab55675e28721ac6e0c0137d7aac4c8b61', 'abstract'],
           'ParallelMeshSim': ['d7810b69a76a231b66f43f753ea4353a99ee4b0b84d2b9797e93d4284f47fa4e', 'parallelmesh'],
           'MeshSimAdapt': ['de4d24a49c777f09e03ccf80d6f274f5ca8c87654295e0e719290419b872fbf0', 'base'],
           'MeshSimAdvanced': ['ad5c7a9ac225161d683a82404effe19aad39a93b5dd1745aa8abb47710a18d84', 'adv'],
           'GeomSimAdvanced': ['61e56850e01ca74c97a1e985297a04e2bbe55084d73181fc1b897eff1afd1259', 'advmodel'],
           'MeshSim': ['d70458a20437f011865526a9c44116f09c786bc05fe0daa9d88a53d3f8e62067', 'base'],
           'GeomSimDiscreteModeling': ['4bf79ee683cc4357b2cbcaf1a41d73f3b3046bf90f6802a12731a709dadd9eaa', 'discrete'],
           'GeomSimVoxel': ['bfab7f861db9adae0436fc467f6926551394f1920c9aaeb7c0994c4e7e990cd6', 'voxel'],
        }
    },
    {
        'version': '17.0-220403dev',
        'components': {
           'aciskrnl': ['a3b47ea8f9525655703f2f1afa2db9ee3243c9c67f259c8c368e0b44d9b077bf', 'acis'],
           'fdcore': ['405fd7abf040e77a882a5bdc29244468a7e8cdd3038e60336a7b96c759a5fa80', 'base'],
           'msadv': ['5cfe87ced8d5bf72512661723f81c1bb9d7c57925ef60c0bd016635d17a2da25', 'adv'],
           'msparallelmesh': ['1421bb9efdb251fd54fcc6df64ad448fa68baac59b15ff4e179db0e728a0e5f1', 'parallelmesh'],
           'gmadv': ['b3fae07ba3b10f64d8f2b9c02e2b3a5a88058afdb439afd6fb4f8c4f0993229e', 'advmodel'],
           'msparalleladapt': ['600b14287009692aff75a7ae07d39b39520a45061f17a5e6800e39ba9a682c5c', 'paralleladapt'],
           'pskrnl': ['6cb506badc1e5ee24a85974e7803cc23c46e7cb24bdba1cdb2fbf7b6105dce74', 'parasolid'],
           'gmcore': ['c2a2b350893dc1b4c33fb170863a727ac1bdb98420479887e617224cab81bf2a', 'base'],
           'gmabstract': ['dc447055f796ef1a0aa6b0ada58ca52ace0ddcea51041e6f991440e3b9a2ec7a', 'abstract'],
           'mscore': ['d8b17b238d7d007b4f3a1e0f5700b4dbbfa348adc24315b1579e65ad8b0e0adc', 'base'],
           'opencascade': ['bc34ce9e9d14e90c412719b19f0c43b132f5e2ca3fd9a672f9d9935bae4f430d', 'opencascade'],
           'msadapt': ['c3b0cf6ff9b69ca7198cfab70c7de4d8c7f773f367eaaaa55e38b06d739afc3b', 'base'],
           'gmvoxel': ['fb6fa0fd6e6cddf56d25695562780b0e8403bb80adc38845ed3d1ccf65a8df2e', 'voxel'],
           'discrete': ['58986d440ec7f8cf939fa7d0a3a078a4b4ec22155ea9e3a607bc3e245f282777', 'discrete'],
           'psint': ['b456dffe6b5e37c99673b9481642d910f2c7703c5cc5247881ea98d6ca14ed42', 'parasolid'],
        },
        'docs': {
           'FieldSim': ['c4ed4ef72dacc0acf6394a65dec8bfa7e3029502244bc5f135adc662699efa23', 'base'],
           'ParallelMeshSim': ['dc3991464bb80176a0f0113f128363569c59313fd8ee6ac8eeb488a479ddebef', 'parallelmesh'],
           'GeomSim': ['4ea39458efc44a54a32863d03ae74da13d291b3ca7308a7e20d2d1dc9af103ae', 'base'],
           'GeomSimAbstract': ['36b5bb936747412bef94d576ab59843ac30cb2ea90f89549b2a98e224d5d45ec', 'abstract'],
           'GeomSimDiscrete': ['4f6137a6828b71bd61aac11993038f91a26451336c1618ab96863509c0eb9875', 'discrete'],
           'MeshSim': ['84f9f0fb9c83cc01b2891abac59a68539041efbf7a743f8da58539bf110a2fa6', 'base'],
           'MeshSimAdapt': ['0b9c622e28963b1f354bb9c38a473bffc89368d2f417628c0ad8e9a4750ae7ce', 'base'],
           'ParallelMeshSimAdapt': ['ad2bfd94887dc8bc70c26782a7e755b3fa2ed05d151b7839d851db9cf0ffac23', 'paralleladapt'],
           'GeomSimVoxel': ['b10abb7c1b793a823d14e5ff1b9766d05034a1b526f0a763e20ffc5f667dacf5', 'voxel'],
           'GeomSimGranite': ['60118d98c7df7c5cbeda8d31e2c3062ad0a3a4e45781b4b5082bf3800e5f4576', 'granite'],
           'GeomSimAcis': ['86e776578678923e6fe963dd800a4e2281350e28fd67c65879df6b9f795ad034', 'acis'],
           'MeshSimAdvanced': ['aec7d3526a9eea7e1a0322a620dc29f16b4967cb240f512bb5775c179d133db5', 'adv'],
           'GeomSimParasolid': ['1eafd78273ca8793f31e20db393b762eb6a091ec3e8fb63bd9cb81eee752f99d', 'parasolid'],
           'GeomSimOpenCascade': ['768b22f956f429d0cea9a47ab039d39a9409f498d4ea2e3f60cd766aa9953c30', 'opencascade'],
           'GeomSimDiscreteModeling': ['5984a323d649c6d267f308a6f21be97ff1db341ffe1fe28d6afc58d93f92009f', 'discrete'],
           'GeomSimAdvanced': ['41962705f4e32667aa3168ed9d41a14a59469d309460311233b822d410bfa1d0', 'advmodel'],
        }
    },
    {
        'version': '17.0-220124dev',
        'components': {
           'discrete': ['6820ce780d43c892fbc262f4211eae861ba1ee5eefbdc1c92bdcf5813acd526a', 'discrete'],
           'aciskrnl': ['182fc78d238b28d43fd9d3f92d442f049942a374ccab4df0c045382d93ef34f2', 'acis'],
           'psint': ['f24cde904c37ebd92c5ab2813176071ef55b3257c1bf835d8ddaf3d77748a35e', 'parasolid'],
           'gmabstract': ['ccab42a4f28b6ba39f59b48e79b06533e9be822802b37457b129c66d5891a0ac', 'abstract'],
           'msadv': ['14de859e3ce820fb2f946dabc9ba4a57b37fd2dfe47918076c1069e7c5de0c21', 'adv'],
           'msadapt': ['40ceb7fe9bfb2eff98fe2c837f752bc76320a39a5ef0f18269a12385039c1add', 'base'],
           'gmcore': ['f4087d231def1036a84df0fdc08d3117a55951110545b190cf1461a08b7bd215', 'base'],
           'pskrnl': ['be237ec189f16d560348a92429831f853469f2bb3eee8dcd0d0a6b45d5b7ff08', 'parasolid'],
           'gmvoxel': ['00ca660bafb34e01e3a54b53046e91e04abebdda0de3318010af94b4542b009b', 'voxel'],
           'gmadv': ['0c2db01c2868ac5fae224448f64b57bfba16203c13a7e8ed0708ab0a57a365d2', 'advmodel'],
           'mscore': ['085c92ea668da0195fdcb6bffcf774548626a051a013c1c6c73d55b94f984128', 'base'],
           'fdcore': ['288c7ab124e174fc3214e0235d5c39fb831cc5b480a2c7c7b609e92bc1785298', 'base'],
           'msparallelmesh': ['b3758fc8b9d3628b2950d218574bd447b39729ab32bd5702be32f2e1019669a5', 'parallelmesh'],
           'msparalleladapt': ['3104929b0b67225cbf65bb6d77efe9fcb0d08e0a4b7273a9c90c8f6fc9e33eaa', 'paralleladapt'],
        },
        'docs': {
           'GeomSimAdvanced': ['7c9c0ed77cb716c870a9d7c08a7224efc456885743192136560ffced1bc15283', 'advmodel'],
           'FieldSim': ['80654fbc1cd10635fa8a236c9de69009d8f8d7e12f06d9ca6135e9b3ea124271', 'base'],
           'ParallelMeshSimAdapt': ['c22538ab2b31becef83b17cf287d8c77ec5729ed1e9baf68bde4d6a3538ad893', 'paralleladapt'],
           'MeshSimAdvanced': ['c69f8238890d11ea67c294b08670d715a628e7cd87d2553528bc2b07b2edbd43', 'adv'],
           'GeomSim': ['6dde9f05c21eaa17faebefafd4e47a2aa87131f106580c0c5eac8c8a6214ffef', 'base'],
           'GeomSimAcis': ['6ed831e74e1d0979e4484aadcb7f8b18629e992e22dbcdb4b942084d7807dc68', 'acis'],
           'GeomSimVoxel': ['b8bf43308bf206ad77e2ba308c1e3bf394fb3210610770e5876bde1389d3cadc', 'voxel'],
           'GeomSimDiscrete': ['d6394a22a213e64cc5e3ad9039f25a66f89798e1b3a543c562764d7e4602e4f6', 'discrete'],
           'GeomSimAbstract': ['b43dbf773265e45c70195332e3a51fe663bdb78d9a6c2bb30420a182bc9fde0d', 'abstract'],
           'GeomSimDiscreteModeling': ['95a0e5950e3d7e6260235b4fa29b8240aa774ccccfc61c24dbe0eafff44630d5', 'discrete'],
           'MeshSimAdapt': ['1b0237d3ca9b34fd6bd0b7f189ac1db6a572753589fdc2c7186abdf14c33b2c6', 'base'],
           'ParallelMeshSim': ['2abf71061e664a8b55929ea88280014f0f4666ae04b63f94d6be0c51a41c1e7a', 'parallelmesh'],
           'GeomSimParasolid': ['4022cd2f1eedc9b9f0e2dc82814ca2ce96edbbbe30f89bf919011b3e0df85bfa', 'parasolid'],
           'MeshSim': ['7c08d4a99577e90fa27f15495b664ca852103e3c42a03b80b8a3cb1b48623659', 'base'],
        }
    },
    {
        'version': '17.0-210808dev',
        'components': {
           'discrete': ['6d7c64add59e5f1b36bf65ab82ca97c87d56793ecd92a74bf2b84fe37bdd5949', 'discrete'],
           'gmabstract': ['5e722c4196db470b8cd2324566678bafeddca07eb5c649b36401248bbe1bd806', 'abstract'],
           'aciskrnl': ['accdf629f3a1424240c41d650c592af5f2913f1d619b272cb88c1b6f0b0bb497', 'acis'],
           'gmadv': ['525e1413d16ea45259813c604d48b60c4c8d417dbba5f63140129a1e91c32687', 'advmodel'],
           'msadapt': ['dbe79cd6c2a22edd7e4ddcc1f7e6cbdd8e13f5ed0112038e3ed30071f63da351', 'base'],
           'pskrnl': ['8555c63aa494a4d213bd25853a92a050cc9158478831d0c4ec4d547f4d0b4a85', 'parasolid'],
           'gmcore': ['3c0609e66530c0bb24c7c59177e9c053e7abd710ef4c113a2eac9e466b4cb06b', 'base'],
           'gmvoxel': ['64148f3ca747007d801266133ec5bbb21242a9bd08dedf23423a6db15baffc1e', 'voxel'],
           'msadv': ['b37a7e8359581914e9a75123a753751f5adc460c40c129ead15f1851dd27cddb', 'adv'],
           'mscore': ['9a15b1bd9f07b57e6986283380b36912e41a40ee12d15799d6bed8265a11ca80', 'base'],
           'psint': ['70ac16dc2551b46f5edb3cc298764c81c674de81a09ab071c100ae3aa6d09009', 'parasolid'],
           'fdcore': ['7209e9dd5d7032f37ce25328d53d2bee690ceb1458220d9aad390162c4cc1459', 'base'],
           'msparallelmesh': ['3c8aaab0d3f4b645faed120468188067f1521abb1ed2470311bb4eeae36d7772', 'parallelmesh'],
           'msparalleladapt': ['2f88c62f4a04b8bb19598f7d0a5068f03f429d2c43937022e1f74e296655ab3f', 'paralleladapt'],
        },
        'docs': {
           'GeomSimAdvanced': ['7aca1c8c37f5baac8038dc51d6780d967e287e549336c42f011f8469329bf5ab', 'advmodel'],
           'GeomSimAcis': ['34beda9bfac575ce3868dfa7b437654cf25e039a9e11f94f6ca357525ec9d74c', 'acis'],
           'MeshSim': ['63098724d79dec6fdbf6c997a0321e7a8e583f97f333dc090b64e1445af8c67f', 'base'],
           'MeshSimAdvanced': ['237e580e3517c573164fb6286140c2bd0f2836b70b8755962e68ba03324a29ff', 'adv'],
           'MeshSimAdapt': ['9a2cfcdd243e62c9fcea688db0b956d49407d813ba2c5678776145b7f702b087', 'base'],
           'GeomSimDiscreteModeling': ['8575a4e2aa8797d528e87da8e5f4af909905f18c1c291f96e5745d87062922a6', 'discrete'],
           'FieldSim': ['5986bbab4da73edf18b639c068e7d61a2a996cefc264eff09a78a0a7ecf89b18', 'base'],
           'GeomSimDiscrete': ['70165be895d209b6489cb2fbee8c71b154552cf1331d6c2fe815e0829c3a1714', 'discrete'],
           'GeomSimAbstract': ['87869c2ad26dd1871746e3b11f71bb490f3503e067f6ea6e5fb03426fdcf68d1', 'abstract'],
           'ParallelMeshSimAdapt': ['0a169e22b7e9d8454d501c37dda6a681901f2b56246ba5efe42f7822b97e7ea7', 'paralleladapt'],
           'GeomSimVoxel': ['59cebd4206492ffb2212ba984dac667655bd22f1796c6569fee55140d90f6b7c', 'voxel'],
           'GeomSimParasolid': ['b9c31588086f5becc093f675fadee86835f008e710f7ce7fab021a6796ccf209', 'parasolid'],
           'GeomSim': ['5fe79e148eb0d663eb5021c5fdabfe2f87314e4e8c68fa3cc6cc059e225dda6a', 'base'],
           'ParallelMeshSim': ['1a35d06eda2c652d889e4dde9a568272244fd813d97aed8f3d664dbf6f5c0dd3', 'parallelmesh'],
        }
    },
    {
        'version': '17.0-210727dev',
        'components': {
           'msparalleladapt': ['e07cb2930d51ed2d7693346d6c08921c686f8f89a8c6cb07b5977118e3992a72', 'paralleladapt'],
           'gmadv': ['e0587bd8f8e9ba1f808c8fe7e8b840177553c73e8b3f233a915ca2d71a90b843', 'advmodel'],
           'gmvoxel': ['772c3e61381ddc49231bab272981ae0f7449bd19a055bbfbb44e01fa858ab601', 'voxel'],
           'msadapt': ['aa5bff6b27b213a0322ccf7933464b71bbde0afddd60f13b4893f441888890fb', 'base'],
           'mscore': ['79de7a5afcc29c4645efb714d3d357c0747d343745de3db999ea3941a50f9abf', 'base'],
           'fdcore': ['8080a37eec4a29c2ea009164e5eb2ca3d5033de49ebe246841c6a6c343cd8137', 'base'],
           'msadv': ['9015735a76a61e2e1af40515aea887b8a601296409e8cfb20f0fb73882687cc8', 'adv'],
           'psint': ['91aa7f71ee5a4d1acf68ea0cedd9a901483c4f2390be064d2e37fe6002f7d944', 'parasolid'],
           'msparallelmesh': ['ffde992d9bb2414d4170de4c535d227c34b73bf271eb652c640f89a43db92d71', 'parallelmesh'],
           'discrete': ['b0d3878dca97fa5057d71bf726c72dba65743862ec64e9968f9726dac3027145', 'discrete'],
           'gmcore': ['513eed0b70bada923e214e515310da8dadfc047841733af9da7ab029cb3f2c03', 'base'],
           'aciskrnl': ['e30ecb41678c3b804f2bc3f3061ad3b49cd5d25dc4236964f96244968a952e95', 'acis'],
           'pskrnl': ['c43f5cff4f3c8bdcd044118b853079d51a9f4b6c27356de577b70ff43d5cd6af', 'parasolid'],
           'gmabstract': ['6f5ac14e8fd6f802ab2b547ff68323c0ab614050a5ff8f27ca0cb447683159ae', 'abstract'],
        },
        'docs': {
           'MeshSim': ['bc4ca66ad6d58953300d013b25cb86f714afe5ea415184bf68adc467c7acb2f4', 'base'],
           'FieldSim': ['c343cd6bbb9cc8b9bf8684487b61f960559a0fa80536532002b993c4a7a5636f', 'base'],
           'GeomSimAcis': ['b858bd1e5320b8ead8306c0a5ad6aca08e521019e0bd4920da8379db51f8d73a', 'acis'],
           'GeomSimVoxel': ['f51aacfc6062d66d0a70c3c80519ac417d262c4b870cb880d5c6860b5a8acf3b', 'voxel'],
           'GeomSimParasolid': ['360d556ddf8214418a2c60d941a5337dd27a2666471139f117e5c0e7b036d89a', 'parasolid'],
           'GeomSimAdvanced': ['cee017222eccc796201077be7f9a470cc1098716fcc6a930e772aaffca427c50', 'advmodel'],
           'MeshSimAdvanced': ['7bf289be9c2bf2e7c21c8abe7a04b325193277359a817c2d39e082226938750b', 'adv'],
           'ParallelMeshSimAdapt': ['bfdf9608d2601c10faead6790bcb364cb5b4e969081c473385b1d74cb8b0f1de', 'paralleladapt'],
           'ParallelMeshSim': ['a71ea944e6868293a496d65d8e82ee84cd6f871047e3f07af81cbc2dc62d8304', 'parallelmesh'],
           'GeomSimAbstract': ['b994ff70ed1c5844efbe8536d7d5f59c95f8003d596f00ce5368d33538c6d53b', 'abstract'],
           'GeomSim': ['5ba2b98ed6a4ee9a7bc82886bb7e2bd807059f9b7b0ccc3d06719b377201961e', 'base'],
           'GeomSimDiscreteModeling': ['5436852f9c23daf6d535a61fa077897fc3ebd83eb2923a6da6e724e4a28c2edb', 'discrete'],
           'GeomSimDiscrete': ['cf24241b50adb9ee1436ca7d54c9fb5dd6ab5e86a590f2ba25af48ceb2744b06', 'discrete'],
           'MeshSimAdapt': ['59271c132aefd28adbc136c47ef6665c635d875e8bd14d6856538ab855e58669', 'base'],
        }
    },
    {
        'version': '16.0-220312',
        'components': {
           'msparalleladapt': ['cc6d6ecba8183f3444e55977af879b297977ff94dd7f6197028110f7e24ea60b', 'paralleladapt'],
           'msadapt': ['ec4a985f9b29914411d299fecfb1a994224070480be5de5f701d9968ba9da9e5', 'base'],
           'opencascade': ['008e7232ee3531b70143129e5a664f7db0e232bad9d11d693d725d39986a8aa4', 'opencascade'],
           'gmvoxel': ['4a74c54c31e9eb93f9a0c09ef3ac88f365efb19666240374aa6d1142db993a2c', 'voxel'],
           'msadv': ['d33b591147152383130cc2190f1bd7726cb9ea3590468691db3be5815802d888', 'adv'],
           'pskrnl': ['e154c22c01ecab2e041cf5d87fcb23eab074449dae7f677f17e7863b6da70fdc', 'parasolid'],
           'gmcore': ['d9ed89d07d83f2c23eca6a27fd9000fd4c8eeefa70ac860aa28a40000a6ec93e', 'base'],
           'psint': ['5c236e429f28a36a36cb09ec3f4778dc7b6e72447014b684792eea733bb21fd5', 'parasolid'],
           'msparallelmesh': ['a791f4464da54faafdc63dbcaf3d326ffc49c9ea8d53e36cc57c15607cf72db9', 'parallelmesh'],
           'mscore': ['48e367e476a03a9fa5389830a6c60824b5d620d04d87392e423a33a331ba3595', 'base'],
           'fdcore': ['022de14021434d90daee8ea1200c024d98a7eb01bb9cb5a06a3b2f7ffee9c0a1', 'base'],
           'gmadv': ['6232ec08ef5cff4269d066b035490f33c199fb545355836ef1536b1a00179b2c', 'advmodel'],
           'gmabstract': ['08a6c7423ed59361c5330dbe00b8914d1d55160de73002e7e552c45c8316f37a', 'abstract'],
           'discrete': ['f5ae00688cf202e75686955185d95952e7b581b414dd52bfef0d917e5959ab22', 'discrete'],
           'aciskrnl': ['c2c7b0c495d47a5662765f1b0c6f52863032e63384d85241e6313c4b773e9ed2', 'acis'],
        },
        'docs': {
           'GeomSimParasolid': ['3420fcc1ac67cff8f46b79553cfe478f34676b9b0cd1fa913255b48cbdfd6ad4', 'parasolid'],
           'GeomSimAcis': ['77b31bfb368f1e7981b3a81087e4e287c560e0a0cd08920b36dc81fea25bcdfa', 'acis'],
           'MeshSimAdvanced': ['abeeb0cb10cf3074295a880412e0568b653f2784b1de19f0f8ede5eec536a8bd', 'adv'],
           'GeomSim': ['b1e762111eb8025b966b0aca4bef3768325d9f1c1e3c72a1246b59539e444eb2', 'base'],
           'GeomSimVoxel': ['bc43f931670657a2cae79f9a2a02048b511fa6e405f15e583631e9f6888e7000', 'voxel'],
           'ParallelMeshSimAdapt': ['dd3a0fd6b889dadb45f9a894f684353fffa25bf15be60ae8e09d0c035045e192', 'paralleladapt'],
           'GeomSimAdvanced': ['3e971ae069baf94b38794318f97f16dc25cf50f6a81413903fbe17407cbd73b3', 'advmodel'],
           'GeomSimGranite': ['e438c19bb94a182068bf327988bd1ff9c1e391876cd9b7c74760b98cbfd08763', 'granite'],
           'FieldSim': ['5ede572cbb7539921482390e5890daa92399a5f1ee68a98d3241a7d062667d9d', 'base'],
           'MeshSimAdapt': ['c4be287da651c68e246034b28e141143d83fc3986fd680174a0d6de7b1cc35ab', 'base'],
           'GeomSimOpenCascade': ['34a8d628d07ab66159d6151276e93fdabfcc92a370f5927b66a71d3a8545652c', 'opencascade'],
           'GeomSimDiscrete': ['d2b11367334401ec57390a658715e91bbf3e3a0e8521fab1ad5d3f7c215b2921', 'discrete'],
           'GeomSimAbstract': ['601b0179b65a385a39d241a9a4e3074e4f834c817e836bea07516015c769e666', 'abstract'],
           'GeomSimDiscreteModeling': ['619b8254d8e3bcc94e84551e997b577dd9325131d084c3b3693ab665b7e4213b', 'discrete'],
           'ParallelMeshSim': ['5b74b9b5f9290111366e341c12d4777635e375523d42cb0a2b24aa1bfa8ab8c4', 'parallelmesh'],
           'MeshSim': ['2f1944e1853a550cc474201790555212e4b7a21d3675715de416718a789ccae2', 'base'],
        }
    },
    {
        'version': '16.0-210606dev',
        'components': {
           'msadv': ['749678abda9f747221d4c8cc3734cb6d371aaeb808d935be8fddf6875304bfc3', 'adv'],
           'aciskrnl': ['1a382d568a8d1d0f36fed5b69f4a5306e7557c8cca16a9b460e67b2bdf7cdf5c', 'acis'],
           'psint': ['7e154d95cef443888077ede085c4517403bcaa3af7a2d0b5ed76456e45e4c0ed', 'parasolid'],
           'discrete': ['33070181a5bb494da9d39d118edbf9d0331768c4a8d3906bf162426bd69f7a2c', 'discrete'],
           'gmabstract': ['e16b37319d8be0b5d4b41dc6bfd531d6822957795199d5570004aede9d4987a6', 'abstract'],
           'gmcore': ['13e39855d7b44df377866de659cf9d441795ae9009eaa0db82c09ccbeda31e26', 'base'],
           'pskrnl': ['dab103521c6b1341000c7dd1fe84bc1a28dcd71cfa578ccb29a86db5038cce7a', 'parasolid'],
           'mscore': ['61b79a500b30f1304e200ff5a4c4b7be07a529d687cf18576680d48b7c65c970', 'base'],
           'msparallelmesh': ['ba4e9917413045c3e50ff02edc75f9f06e1d4519556b5fee0d396b5a0f3f7bc3', 'parallelmesh'],
           'gmadv': ['94bd3a9c5df1d3acad4cda4b6166db018df1273b5ab538abb9f649fbe7e98918', 'advmodel'],
           'fdcore': ['ba5432400fa205054bde4c3ebb4438ec32ebf031017fe5e0f46361bc31c760e2', 'base'],
           'msadapt': ['ee43e52bbb19bd4278a19d3738889ae672eb8124484a5d248db814679d1b376e', 'base'],
           'gmvoxel': ['6514cef5858bb8029c21ccb385502e3481231210f28d14d5fb83a1c66f48dd11', 'voxel'],
           'msparalleladapt': ['0704fa2f1923f4722b4ec61e126fb67c4725632a32240eb9e1d52ea271151b36', 'paralleladapt'],
        },
        'docs': {
           'MeshSim': ['37021c6b0904cdaf61094334115f0aaa83624b792fdfb3c9f5c6eb4cb629a891', 'base'],
           'GeomSimDiscrete': ['77bf38fa733639d4509dd890e7c953a807caeb1fed8ae9120d2d55308ce28e30', 'discrete'],
           'GeomSimVoxel': ['1173f40ff8c9dc57785d9dbc13b3c3bdda50888af46dd307b6aa99e849f1a630', 'voxel'],
           'GeomSimDiscreteModeling': ['91dc959b95ef78dca29c8e52ef25eae79a40003a4880673af34be958a473cf14', 'discrete'],
           'GeomSimAbstract': ['a4f43a52a7dc52ac828f6b2ff0a47dbb46c3c4643ad2610cf344bcb470d52d39', 'abstract'],
           'ParallelMeshSim': ['2051150a6260a9c5890a76c63e8c86ad10c6a0775fdb07e87a15d14248a5f1d4', 'parallelmesh'],
           'MeshSimAdvanced': ['47b0d7219fd86b78ea0a2633805547e50528e9f278904f6d73d12a8f2802dba0', 'adv'],
           'MeshSimAdapt': ['a1c923eb9cfe27f0cfbf21ff6ef9bcf265e0e27a80ee92e0b4d6043eb3c8936c', 'base'],
           'GeomSimAdvanced': ['64dc55cb7126083c5d2d87e9fbd04e37e3155add759f828793954b29fed8109f', 'advmodel'],
           'FieldSim': ['d8a04e16172e645750b6ffd5fde59f4fbb130c9c974505c2ba1d62d415039242', 'base'],
           'ParallelMeshSimAdapt': ['a837267a77bf89e5955f6c13b581a42a8a427272eae086a2653b7c06423e9f2f', 'paralleladapt'],
           'GeomSim': ['1966a6dc1ac3c6c025df044b1a51e56880c5b65d0dd615a2a362b4dc7c9c945d', 'base'],
           'GeomSimAcis': ['8c78c6a1ca188e1aba5695bdceedaec15ae8c50c32c5985e7930f7dfd9404951', 'acis'],
           'GeomSimParasolid': ['27564ed05c85d8064d251362efd4724836ddfb00e335126cdb5a6f1b9063b783', 'parasolid'],
        }
    },
    {
        'version': '16.0-210202dev',
        'components': {
           'msparallelmesh': ['8c940c0801f361ec66c345234a72352fac77112a539b2c766d9201c8911c20a3', 'parallelmesh'],
           'msadapt': ['aeef732ddb4f6107804b189aab3a7912401be97844d5b5beb7d4d4630db77894', 'base'],
           'msparalleladapt': ['79722d2ba104338fba9345f38bd87eb36f6ff9e431f6b886369c9fbd07fb1115', 'paralleladapt'],
           'gmvoxel': ['e7f6b49fcccc3080d0a73a7a365e0dbd63f66823908e79377a6daa12778338fb', 'voxel'],
           'gmabstract': ['6ce2fd9beb374aa6c805b191ed8b6a40d93ebb0817f879fe4cc5406f80d41ca2', 'abstract'],
           'gmadv': ['6b8e96778c88c999e310618fdd9b2cfd45f6a73ce3ac87659ca9ce42e5f8f2b0', 'advmodel'],
           'mscore': ['7a573af5b3f3c9351e864f24dd9e17c153972a6e2c426f723213e22aabe811bc', 'base'],
           'fdcore': ['1a3bbf8f9dd8bea1fd7d7a167bef12a3e35e21295d6329c3ea0c8d4876bcac00', 'base'],
           'pskrnl': ['d26d9b18ade1a3ffb2966d2602701400219fc1c1a3c11cafa03b999fa2c0aaf4', 'parasolid'],
           'gmcore': ['8bf745f432388f4ac286b7f3840eb9842cc858877c91fba8f3fa508c02e76424', 'base'],
           'aciskrnl': ['a807df895af622c7758ebbd1fbddb955871e618d5d9ec916911704253389d2d5', 'acis'],
           'discrete': ['7b24b37ebe286454d4a6370d8bd1dda62db1b84c38afcc7fe8db30c41ba00521', 'discrete'],
           'msadv': ['e089b1f3d2d8a854ef2e621df89ec2b3a0e8010507f0985524740f0839ec1d20', 'adv'],
           'psint': ['d446337f67c48197a42ec7fd14669b20cc44fa9f2057a4fd2d48bfee7e83ace4', 'parasolid'],
        },
        'docs': {
           'GeomSimAcis': ['8ba3d9022e8736c917dd453fb0ee3af2dc7f5bd92aa623717fc6c9361f8fce33', 'acis'],
           'GeomSimAdvanced': ['37b91a52b8ae7806bfa87be2ea6136102ca2896693ea62842293a30351559eae', 'advmodel'],
           'GeomSimParasolid': ['2b9c05e6522977a365f24d4b73630871bd087f07dd19e668809c389f5fd006a2', 'parasolid'],
           'GeomSimVoxel': ['744765e4a3aacf4339612b93e87d5713312642f2f82694eda6c3cc146b4f4e89', 'voxel'],
           'MeshSimAdvanced': ['c2ac8640af585879dbb06fa168d558f9f859d495c3dc9a2c22eda5e9b413a73b', 'adv'],
           'MeshSim': ['d973c0d0909ccf8a186d8d1551b22b66af577f5676e8963624aafd7b5c659a20', 'base'],
           'ParallelMeshSim': ['40301df2e52a792a99b5afc9eae3254311924534f7d26a5cbdd4d590f9a9c0f2', 'parallelmesh'],
           'GeomSim': ['b67131c23bf748ebc4f8f945db598f90a2ea0ebacd81d881a4b4d301315f42a8', 'base'],
           'ParallelMeshSimAdapt': ['170815c74eb618155ae677b46e45e1e0aa1276110bd68943cf752f92784dbb70', 'paralleladapt'],
           'GeomSimDiscrete': ['56179e9bb9ab3ee65c84cd31e71ba1572b8698ec2e4a04a1839b516507f0bd30', 'discrete'],
           'GeomSimAbstract': ['20ff7443da35dbb9c309d051026cfb932d785f09f355739d788c936b5f54291f', 'abstract'],
           'GeomSimDiscreteModeling': ['f11f76a9ab6c5d6cf71d8bdfae9a65697210707c38507e70392b0f933f326326', 'discrete'],
           'FieldSim': ['88af2af86ab604eed86fbae0d7669e17c633c2afaaa1ae40e4f8621dc9fc1633', 'base'],
           'MeshSimAdapt': ['cbe281fc84da0bf2315cd5143faeef1ebfd4f762370af97f705cf503f4379599', 'base'],
        }
    },
    {
        'version': '16.0-201021dev',
        'components': {
           'discrete': ['7f0b4a21f06dc8c4da16d11188fe4ab7f073c05134045b93c74ac21f0bd35a00', 'discrete'],
           'gmadv': ['78ddd410c15aaaff720f9f6aa49f928f94e6a64c71f46bd8c2ce06de82544896', 'advmodel'],
           'aciskrnl': ['34a4fd820b66ee10b5b8b8a66596e2e393ee51142bc267b404ceecc51fe67b38', 'acis'],
           'gmcore': ['4f31f5b91522aba7ada140430d2f9282c0be71148f505fcd097be8f7bccb0480', 'base'],
           'pskrnl': ['03ab668572eac5e077016ce676370338455d504fc4c3599f03d6fa4be3377b99', 'parasolid'],
           'gmabstract': ['a9ab6cf16ebcadae423547f6a2baabf6987069eb880645ab2855b013775599ff', 'abstract'],
           'gmvoxel': ['4bf99bbc0490ef637e54a84ff9758e965e006dac5dc7f4dfde3d0a6dde25f770', 'voxel'],
           'psint': ['ae8156a68a970aa56c15b2386f595dabb3f52371143aeeb77e7d5029a5ea84bf', 'parasolid'],
           'msadv': ['d008e67b7517d7bcbbc54a1f5d80b547a2ec9aa3960a4ebec39fa29da2190af8', 'adv'],
           'msadapt': ['44fc32bd4b9cbaf616ebf5c6539d0549a5538b5078711ce8fe2f7bd0267e79ef', 'base'],
           'mscore': ['3db8836a8d47c1d78e60515ff9b5e9fe39fb9fa9221cb13b42ee15a5fcf9f6c9', 'base'],
           'fdcore': ['e66aee5ddc7490d9b0ad138dc2207017bc7bd284a7a62dacfa9102aafbe424fc', 'base'],
           'msparalleladapt': ['21f32512bcce6ffeaec06e14b74f5cca4a406fb7cfd1f79c6314614462103bbd', 'paralleladapt'],
           'msparallelmesh': ['81582621b55fbeffd9e8a53acf01d19763b3e97a4064fc18b584b61d1a3cd828', 'parallelmesh'],
        },
        'docs': {
           'GeomSimDiscreteModeling': ['8e6a8521d88b51edcfe8840f0988519cdfe82df9d83481b3dff14d9cc3346b05', 'discrete'],
           'GeomSimAcis': ['ab22b500ae07a002522bfcd11ebf0a764a8766910c4dedbae670be53a55aa0ba', 'acis'],
           'ParallelMeshSim': ['735de87a46a7db39214fae537907eb988b2be2400ca1764eb2e744eb79ce28f7', 'parallelmesh'],
           'MeshSim': ['813955d0f02110ce1ab7d107d440f07182e3a71811dd0492d95d50fa2a1acdad', 'base'],
           'ParallelMeshSimAdapt': ['e94257d2927bedf00e6a28cbc60952506c9f9a73557d28fc2bd503f3fea1fcec', 'paralleladapt'],
           'GeomSimVoxel': ['f874d5cb6b6b14e02dbf199cb93dd508f900da4e47d9727ccfc1af296bd953d6', 'voxel'],
           'GeomSimAbstract': ['c77c676c11914cd8a7889a1f81512915a6df42d7322e4cafa64e060704625ddb', 'abstract'],
           'GeomSimDiscrete': ['48f29b4723ae441edffc7232daa5ee5359e21ed1d0a19a206c9e9da416d63fc7', 'discrete'],
           'GeomSim': ['4ed35c75b4bed3f69bb6e715c89e227c7141fd180dbd1e91136a819e812cf1b5', 'base'],
           'GeomSimParasolid': ['58a920b93ef8a7d8e4fa9bc27ead90304b0fdf9e692c7a27da27783277f71dac', 'parasolid'],
           'MeshSimAdapt': ['d7754ec435af5307052b6f6e2dc5cbdce44602e8e3a8da645749697312db8d00', 'base'],
           'MeshSimAdvanced': ['c1e0bf66472ec2c52148dd2e1e1e3616d599faa217df743307b6ef4fcabe3592', 'adv'],
           'GeomSimAdvanced': ['6b8ef231f2ce06cc9d02f8285102b30e2f79e1a7bf22f540137fc15c624b3dd8', 'advmodel'],
           'FieldSim': ['a71abd1be50adf20bc3cc5b3985a1697451ebe66dbdc43c46d85bbc58b0232da', 'base'],
        }
    },
    {
        'version': '15.0-210501',
        'components': {
           'psint': ['5b337903df385c150a8e823007fb236a6d1ff3c4e6fb7bd6fa551c19d4e91e0f', 'parasolid'],
           'msadv': ['ca49734c671a62912e4463f41aae522fb6b9c1db8481f4dd885e7968792d88c9', 'adv'],
           'gmabstract': ['8da2f8fb228477e7a038adfe6338f596b9e1711a5c8e094d128ae6881452ee01', 'abstract'],
           'fdcore': ['acc0b2af0fe7163e1d63bcbe9a874b1a64beab119192cb73246965686319f6c4', 'base'],
           'gmvoxel': ['e1caf8cc569c0aae6d51991220f66fdab73ec8ecec98966eb428629e67d36f3c', 'voxel'],
           'msadapt': ['58d76d0b37a220a97f1246fb2bb9733e1ebfd9bf21ee57eaaaecfad74313d18f', 'base'],
           'mscore': ['ea5814e1a57f49e47503b7da4bad627e343494a43b457dd9b9dc3fc5d3b49d48', 'base'],
           'gmadv': ['73db91292a256d636c7b636e2c8e8921fc8bf148829aa86d2b5ba9797907050e', 'advmodel'],
           'pskrnl': ['4bc26c4595f640ef537cb812b3d5335d8efc77c1b0e071d150749ea1e13470de', 'parasolid'],
           'gmcore': ['ccb1c9d846843c2b30c84a2e19e6c8db58040fdf78158c3b0c16d8a409d5849a', 'base'],
           'msparalleladapt': ['7eed824dfd4351bdfc346c949aa053cf7aee927059ffa9ae2e610e19cee80b70', 'paralleladapt'],
           'aciskrnl': ['b9143f66755acb8cd394c4ba22856ce464cba7b8ea58be32e1bf2361aa5825f3', 'acis'],
           'discrete': ['3416db2899bcfee77dfdca0c9dd6ddf986f000b93ef1b8dc18a2904061d3acaf', 'discrete'],
           'msparallelmesh': ['874bc64f7b358c965c862a09c19afd9817e55482b2a16676c5e8cb796d25a8f6', 'parallelmesh'],
        },
        'docs': {
           'MeshSimAdvanced': ['7bf6251991fe7e33967c500f7826fb0270553297cd61d26e5af50edebd23d65a', 'adv'],
           'GeomSimAdvanced': ['e92053cad4562c718f366056dabc6c911097850dae98f88f39f193a9668f9dad', 'advmodel'],
           'MeshSimAdapt': ['f67064d20c35690c39a9d25e4bf38ad5643414964629595f568868e674cfff68', 'base'],
           'ParallelMeshSimAdapt': ['6b9f81fad1c60d7351f8b9c14e18a5f9610dd1df3589f6745b7b36ba7af59251', 'paralleladapt'],
           'GeomSimParasolid': ['53197a05fc772ed0ab086f31aa522472cbfdfa0033a4af770d2325e0de15001d', 'parasolid'],
           'GeomSim': ['ee644776e7803de28884d72ac5d59cf3275e1f2546b8caa4c68d0770b673fdf2', 'base'],
           'GeomSimDiscreteModeling': ['4ea593bb276d34a68cc54cb465aa1cfb6580f1483b915493d20c55b79659785b', 'discrete'],
           'MeshSim': ['bb35238f27dff06f65d1f087f87f281e91f79ade07e9eaa78538aed7162ca112', 'base'],
           'GeomSimAbstract': ['3dbec0786fcdc3a7d61d03b59a0a6c735683ad09f28375423f4c98df5c3a3c75', 'abstract'],
           'GeomSimDiscrete': ['484575d1df6927008ba29e2ea9480e13f6763f2c511155a6146fb31dd3bbed00', 'discrete'],
           'FieldSim': ['c4d6fcc303a5e4d593b7ddf2cdedce1e66449f3c0004f8ac75e0c833d330b473', 'base'],
           'ParallelMeshSim': ['ea94401cdc12bb285b3c14cbbb28ab544e7486d786b6d51d8eda27351e900055', 'parallelmesh'],
           'GeomSimVoxel': ['1ea9ad205adbfa917a1cd75eb8f63ebb29c1dacb850af1a19172f37146f16c62', 'voxel'],
           'GeomSimAcis': ['8df8d03f49e9a91cb124e026b4581476eff9dbff41bde3192eb60f2b41d8c48b', 'acis'],
        }
    },
    {
        'version': '15.0-201024',
        'components': {
           'gmcore': ['6ec0b9ec216c1f46d35ecb0352023581d3ab48f93ac747df15831dc8335dfa32', 'base'],
           'pskrnl': ['2025666147e5f5edcee44d7f66cf068579cca5be453b12d2ec295f655ec24c6c', 'parasolid'],
           'gmabstract': ['7bda23e451309c7a27e06814ae0de6455ca36dac73cc0c2ed5ad158b991285ad', 'abstract'],
           'msadapt': ['8f9359efe80ea5e0e8c7c7a97fcd42288ca515ed380c108360690a5ae618e000', 'base'],
           'gmvoxel': ['461286f53d3cf6cd1c6f2d0b2929ea64d93b53c3848944ab173aaf1e8e302f26', 'voxel'],
           'psint': ['0a8224b9acad31a6374b5f7ee0d0a8b1726547a62eedefe71751cabbbfd11ec4', 'parasolid'],
           'msadv': ['9a922c6f17ea1bc7e8652e29bbddfb7a733aee5ddc7ba5f974f18e1ad6ff3498', 'adv'],
           'discrete': ['2b996edb79cc6638c958d1710233f1dd1cc248194818075be476078d91cc8ede', 'discrete'],
           'aciskrnl': ['70c5568dbe4b3bb4516b2183807db43bdc35700919b2d830751a511f4c02c6a2', 'acis'],
           'msparallelmesh': ['12d42bb6ed74c074f77cffa55965f86034d3cb9676c5f831c04faf3d14c17f05', 'parallelmesh'],
           'gmadv': ['803ae8ac785078cc1d123e89ef2b6e3bc5fb8ebc6eb9e00435e9ff2666bbd583', 'advmodel'],
           'msparalleladapt': ['8324063e0b380bcb943d6aeeb6aef06c66301ad62aeccc893ae70235976d0b82', 'paralleladapt'],
           'fdcore': ['88338af2b4c1129496aca01745effd77f546330a95b7596503b814309edb3d78', 'base'],
           'mscore': ['5cba49f1aa7a17150b40ae336db86cfec8363038a972f1221ac1726ef3fb407d', 'base'],
        },
        'docs': {
           'GeomSimAdvanced': ['35ec6063bf336b0537de71914c31a7ce3b41512b40256541bb722f0f873e7791', 'advmodel'],
           'GeomSimDiscreteModeling': ['14f691e9e6ce8d65d150a9984cc65a227f118f0ad20f710b0145d4043155b8d3', 'discrete'],
           'MeshSimAdvanced': ['a9c374ff4a49c2786828e5d314fcc049ac442679a1abdca95e45191f87cf48bd', 'adv'],
           'GeomSimVoxel': ['5db0965b03c6fa1bff762b01c21e8e0859f89042e0643ed427fb641a301922a3', 'voxel'],
           'GeomSimParasolid': ['b37ba23f5ab54de824db1698d44b906ae015c283709e765d231526bee6af6743', 'parasolid'],
           'MeshSim': ['f0efa2c402cc6847d1cfe2be3aebad4c3b19e7bdd240056e412226eeb08baa98', 'base'],
           'GeomSimDiscrete': ['69529bf020fc1136d0a0be78201da76af66dcdc4fd8fedbc92d7a565d71648ec', 'discrete'],
           'MeshSimAdapt': ['cd7adcdef3e104d5407372ee34e631f7fdd569d2dbdd437a21f52c7ff204d130', 'base'],
           'GeomSimAbstract': ['065b85a40214a6d6ed0267da9b592ea7c5c1271c5ced360bc1b84b8410356277', 'abstract'],
           'GeomSim': ['c2daa872b529a4d95e9be0c266db362008b1acb27c2f29b90ef5ac75ff296d46', 'base'],
           'ParallelMeshSimAdapt': ['838f78573f2439ce32029c49c55c5551184b826dce11951b662776fdc2e45873', 'paralleladapt'],
           'GeomSimAcis': ['935636750e43fd06cef25548bc0b2ee0f413c50ea8d5ad5cd568df80ca565620', 'acis'],
           'ParallelMeshSim': ['1e6c5de51425a1941005f0f1cb05ea97d432baf90b8c3c84a696aa5332e388fa', 'parallelmesh'],
           'FieldSim': ['861df6f04fefd8d667c6250f9a6441314c2e337de1fff6de0aa0e7a3e5d8a52d', 'base'],
        }
    },
    {
        'version': '15.0-200714',
        'components': {
           'mscore': ['406b12403bd4cdda47423c671442cd608bd0781e453224250a0fc4bf21304aba', 'base'],
           'gmabstract': ['7f65e299f63b09cea80eb8a6530b20b3d4e63a44346db3941180d00a3b994c61', 'abstract'],
           'fdcore': ['7f11a554fce2acf484646bd591e5eb903e3caf22f7f6bda54edb5ff3f10aef56', 'base'],
           'gmvoxel': ['3a20dd3d0c9d31ac61a6ca8ad3c7cfae7cab44ecab37cda2f13aedab4613eac4', 'voxel'],
           'msparalleladapt': ['a46f17914256d58d2c52e1f39f3e511c97bc2416135d44315805aeaa7257324a', 'paralleladapt'],
           'msadapt': ['75ae6627811ec860c5baff9180b5c49a842cdd7a0ec1f27fc38eb855872fcea7', 'base'],
           'discrete': ['2c5bd5a15263ef8f7460286e68cbf84f72aa5a14e6b4e6a60eab89389e92be73', 'discrete'],
           'aciskrnl': ['f51c32d8dfd9d8188e8a64218d7e9a4d1204d0c3d47d489796c772e6bdd2055a', 'acis'],
           'gmadv': ['dd02a7f2abfaf8394e5dea73b318f361341c4e873b074b54f2e091925d6da171', 'advmodel'],
           'msadv': ['b0111bf553f61dda01b5f418320d6055a8002f4e583370716fdf0c9a4d1a806a', 'adv'],
           'psint': ['15a11c51d9b8a2bda2aacdcaa76aac291c9954a8294ce4cd0174768e2f83ee76', 'parasolid'],
           'msparallelmesh': ['75af607e437303e063f20668ec1b13209cc40c7f497667e5c265870a8e773f46', 'parallelmesh'],
           'gmcore': ['0b7070c81ad04956939da78509f5945ec68d99f5871aec38fe2ea64927445787', 'base'],
           'pskrnl': ['7c20a0c23548238ef6f8aa06d7bc6f448a64b286addac07b144e9fc27a3274c6', 'parasolid'],
        },
        'docs': {
           'FieldSim': ['5b91ef5274b7cce32df5a7edfb7579d0578d143b3f123120b12ed780268580e9', 'base'],
           'MeshSimAdvanced': ['8995ba7d66d06931e037fc5b14a6f9ba95bc1a09a75c88fdce5767d3155391e4', 'adv'],
           'GeomSimAdvanced': ['970cc0a9e45931ca96a2824ed863718b1f77e624acd9b29f2245ba14e9700b81', 'advmodel'],
           'ParallelMeshSimAdapt': ['89a452b3d7b7902e41a82a4facb9162596248570d76ce200d961f1ad0fe2acb5', 'paralleladapt'],
           'GeomSim': ['0a2cfb53c5ca71cd3bd49357f1b06f29d74c3cc9d4bdd7ab54e3cb02bfc032f2', 'base'],
           'MeshSimAdapt': ['90ce56775da2d0e10ab1d2dc52e001fca716cc176733faf53efc16489bd34c83', 'base'],
           'GeomSimDiscreteModeling': ['94c667f2c8675e523cb256e77c01405e3a4db5507dcab8454e81a1f7cb46a5ad', 'discrete'],
           'GeomSimParasolid': ['73394ee10f132997dd2147de7205198b373dfef4dc3502783118cdbed407ebbc', 'parasolid'],
           'GeomSimAbstract': ['26fb1e199ac03231ae590618a02300f0866da759ae8d8bcdef5095cbc942e8dd', 'abstract'],
           'GeomSimAcis': ['a9c6e1be667b3f1a0db24bd213129819e376db78b24dc33312f226737d75c14c', 'acis'],
           'MeshSim': ['4434932a7ee53ebfb1112f4c93b6346374c4b13ca559dd944902921f1cf82639', 'base'],
           'GeomSimDiscrete': ['693c3ca1d9911d62c9707726ba289639251b29f376f56e88479b70a21feb6d67', 'discrete'],
           'ParallelMeshSim': ['a6a8af88e483bf93cfb16eb563d066bf8c547e37a6a84b2957c4604c100771e2', 'parallelmesh'],
           'GeomSimVoxel': ['474fd4853e0565bf1a315c9eb682291f7ade849fda46bcd02e672047260aed1c', 'voxel'],
        }
    },
    {
        'version': '15.0-200330dev',
        'components': {
           'mscore': ['bde4312537462fc4cd7cc811276a870b00e813931e1e2f6de19bda68ac507c72', 'base'],
           'fdcore': ['e2b240faac375dd7c8da500ffc7fb0e752aa427f243dfc877aaaea20609c828a', 'base'],
           'msparalleladapt': ['7d77b93b57e8c6e83416142ef47ba57603fa088cf9db9e3618852425ad593adb', 'paralleladapt'],                                                                                                               
           'gmvoxel': ['4ad88822809480393dc0ef332a4789696104e291979ca9ef278120875f37c30c', 'voxel'],
           'aciskrnl': ['83234ddc24837068285d4486409a14b5bf87dd22ff3ed9773f671b7b63214125', 'acis'],
           'gmadv': ['f3026ad243fe15b1ca43bfe39a91a124c3625e6225bd6c9f8d4bec2a139a25e8', 'advmodel'],
           'discrete': ['5cdc1acf3130b31cf8d13cf4495f69d10031ea6dd011b28de9d4706558714bbb', 'discrete'],
           'gmimport': ['2b83d65e7c708bcf569345fa25ea1c23565ef25e74605c402a5a52cde6b53634', 'import'],
           'msadapt': ['9cf3ab66c3f66e0c0a2d0e21d325a040da56375ffd41c030daea36d2b19c5e41', 'base'],
           'gmabstract': ['ae8c52d59902e0ecf537cbef1c12b1ad606827ec46ed2204b421aa11835b6ef0', 'abstract'],
           'msparallelmesh': ['241b1415f613442f3abc2d26d02480cbeaa3870422f6a0e3c433e3fc7efb5e16', 'parallelmesh'],
           'pskrnl': ['dac2c7997a794002b3de729ad018cb3c9668bd7d6a378a540080299d6e35a4f9', 'parasolid'],
           'gmcore': ['30236d7fca6134d9a53cff00d01b2a65140e90e21f321875419ca8209580672e', 'base'],
           'msadv': ['40a9abac791f2db809d2a36a3e7194479da2faf1e9a3be1c16680a38db81ee23', 'adv'],
           'psint': ['d4a4e4d76bc4b2b56a0c495b26e7b5caf7b9c13a2870cde33d55a05ca41dfaa5', 'parasolid'],
        },
        'docs': {
           'MeshSimAdvanced': ['d0fed2e758c3ebadaac16256a28a6c891e9e125ba8d25e18ca509306d4c1f36f', 'adv'],
           'GeomSimVoxel': ['1b7653fd52c53be6afcb9dca6926e717a5db41de3950dfa9058acb950f0ec60a', 'voxel'],
           'FieldSim': ['2ca320139c7506bbf63ef2599afaf7a711ee5557f5e970d5cf2f54c4a79b27b2', 'base'],
           'GeomSimAdvanced': ['fd1287d72b98dfa6cc94eed1bb5bf2a021416f58cb489ba87c173a5b4cb1b6e4', 'advmodel'],
           'ParallelMeshSimAdapt': ['d2af57fde42a9e294bbd2f16b987c06ef7d5abe2a580a27bd9393624b6459b72', 'paralleladapt'],                                                                                                          
           'MeshSim': ['ca0291e1fd03ef3de15adcba89300fa9129ecb65b34a023a86ba9b1be19ef68c', 'base'],
           'GeomSimAcis': ['d5fe35e792da448294d20460ead68ddd2ab0ee429f2ffd15fcd0b801ab72eead', 'acis'],
           'GeomSim': ['f351fe2fafd9afd4a4c21c6467bd51c6ab6cbbef9a71f772eb4a492670042738', 'base'],
           'GeomSimAbstract': ['4016435b62a1d00baf9f882fb9674f648ca67fe899760fccfe08828feae6752b', 'abstract'],
           'GeomSimDiscrete': ['eebb91523439e29e35a91b9d348b0c7d42438dbbc5652e344a11cf6f21650557', 'discrete'],
           'GeomSimParasolid': ['554e97d44286542c7381672fd9fa2d8ce5642d73bbb651eba2d03b42db5010f6', 'parasolid'],
           'MeshSimAdapt': ['7e7ad0ba0c6ad6ef4a8ecc2f003ad13748c25282c17183f8a40bffd1d71b7612', 'base'],
           'ParallelMeshSim': ['7ce6e9b8ae41e8c626b583efd64f2b34fb21d1fa9e7237786a38f9bfef87d099', 'parallelmesh'],
           'GeomSimImport': ['03897cbb1b04071182e8f45cad75538e7186182fe9432a488863c894c632e2de', 'import'],
           'GeomSimDiscreteModeling': ['11753080e0507baf5a9923d45da463383cd8592f836625c0a9f735f8082ee60c', 'discrete'],
        }
    },
    {
        'version': '15.0-200110dev',
        'components': {
           'mscore': ['3eb4d488f6fc902ceb46ba879d8e1681aeed236554d4e96a002bebff9245ed5c', 'base'],
           'gmabstract': ['6eaf0301011d2b1192136dd85d3ac14e4edfa0c3db55b5c085f566faf40d0483', 'abstract'],
           'fdcore': ['722cc6019cba238eb4b5e810fb3480f54049c0097bff652d7f2877b26037efa1', 'base'],
           'gmvoxel': ['3703eb8745597136208999ec9bfb3f74b972e11be81d5d172c89f9762dad097b', 'voxel'],
           'msparalleladapt': ['dcf01794c98804075fa0eee88956f1211910425659c9677750f6529a4adf73d8', 'paralleladapt'],
           'msadapt': ['8b31bf4eba9bc1da2da6c202b22dcf270139379fcc0b989a5cabc759b58f92ff', 'base'],
           'gmimport': ['222b3f770e8507545181b11f240ef534f1fbcdd10d809f9b36ea8bb64faca07f', 'import'],
           'discrete': ['03ad9e5b0d1a33b4194c24c33008b6de0ddc67180ca07407115864eecc5c55a7', 'discrete'],
           'aciskrnl': ['4a53a24e0b44ce4d90fa933421ecb4e21a151029b430c2af725d2691fc6b3e0e', 'acis'],
           'gmadv': ['cde7c68917c511d84e680ae1cd7350ca3b45aac78c792434633428f023bc2812', 'advmodel'],
           'msadv': ['c1dac43bdec1ea2d3ef0d2a5cd511fe90cbe84be4ce14bbc234e9242bee49fef', 'adv'],
           'psint': ['cdab17a4fa08ed2912922f8b0c23954c46e45c52d67d56ba8e3351a7678125ab', 'parasolid'],
           'msparallelmesh': ['2ea6e9024c91dc536b09f4813696f16ec3eac0806f1f8011fe780ed7b24bd430', 'parallelmesh'],
           'gmcore': ['4301533ef946f4052f3a3f5fdfe5dcce6a2f42863fae8e37f00b5a30ad9e9fd8', 'base'],
           'pskrnl': ['2007f0730af8d22f0f2a059e4893bc2fcfd98c813490fed32a690e53ac691646', 'parasolid'],
        },
        'docs': {
           'FieldSim': ['47997eb18d0a03d230006e44f6d294f994063f6db1bc96545dc1547125c9eaa4', 'base'],
           'MeshSimAdvanced': ['cafe56eb373ea8277ccdded344abe065bde39b25ac15a332d05391788d86dbdd', 'adv'],
           'GeomSimAdvanced': ['746e1ced6a8f65fdb360c1103ffe25660201f6bdfcaf30d9a014f0b3de5911f9', 'advmodel'],
           'ParallelMeshSimAdapt': ['02d5313d570c7d6516deaa3f0880a86af5632e474fb904c1620baee095f12417', 'paralleladapt'],
           'GeomSim': ['3bddb2ecda7f4d1ba56b97e02d1d474f9d86b1714d0a8a0b7eb3a2f07d7a5229', 'base'],
           'MeshSimAdapt': ['49b367c90739a965f85c79e87dd9dfc414bef753ba5c2ba179ca3c91b46153ad', 'base'],
           'GeomSimDiscreteModeling': ['1b38e7728d1120ea2fd7adf88c75c39d1fd7522206fa6590327c24c2dbf27814', 'discrete'],
           'GeomSimParasolid': ['4e28c003d09ce341aae8d205b97aafc764bfe6f03ac4defd52afa88a5a496b7a', 'parasolid'],
           'GeomSimAbstract': ['881390336e458369e7148f1337d46a8b9750a0f6438d3d76d89deaeab82ba095', 'abstract'],
           'GeomSimAcis': ['ea618faaf82462fc90c9f6d5403a1bc493221faee79f547986dda5633745de9f', 'acis'],
           'MeshSim': ['5da925e84d86132e956db39bed4201df7d27bab9eabb3d85ac4b2e025eed6133', 'base'],
           'GeomSimDiscrete': ['63796f464daaf1c591b8c22473e1fd162fad20ef5a2d908c3bb66d6e11410c25', 'discrete'],
           'ParallelMeshSim': ['57c2c7597c502dcaa6abfec5a6daa197b73a1a9cf5cedd71d03a35704cfebc39', 'parallelmesh'],
           'GeomSimVoxel': ['179356ff8a2f3806a0f18e9a30208d3da23270485bae8fc79a08bc083f3b622c', 'voxel'],
           'GeomSimImport': ['d96f6b2e70a5825463726e0ee55e86845cb9ea964e0db85a4575c26492e28b56', 'import'],
        }
    },
    {
        'version': '14.0-191122',
        'components': {
           'gmadv': ['01cea5f7aff5e442ea544df054969740ad33e2ff4097cf02de31874d16a0c7c2', 'advmodel'],
           'msadapt': ['69839698f24969f97963869fd212bdcff0b5d52dd40ec3fdc710d878e43b527a', 'base'],
           'gmvoxel': ['bfea15e1fc5d258ed9db69132042a848ca81995e92bf265215e4b88d08a308a8', 'voxel'],
           'gmabstract': ['dccdcd4b71758e4110cd69b0befa7875e5c1f3871f87478410c6676da3f39092', 'abstract'],
           'fdcore': ['6981b2eb0c0143e6abc3ec29918fc3552f81018755770bf922d2491275984e1a', 'base'],
           'msparallelmesh': ['1e1a431ec9dd85354ff42c6a2a41df7fbe3dfe5d296f40105c4d3aa372639dc3', 'parallelmesh'],
           'mscore': ['bca80fcb2c86e7b6dc0259681ccd73197ce85c47f00f1910bd6b518fa0b3a092', 'base'],
           'discrete': ['430e5f2270864b1ab9c8dff75d2510147a0c5cde8af0828975d9e38661be3a35', 'discrete'],
           'gmimport': ['e83b3c43b7c695fa96ed42253a4b317a2882bcb8987fd3225c09492e353e49aa', 'import'],
           'pskrnl': ['31455cfce746b2339b3644f3890d4444014fb839654a9f576ec747d28ff6c1c4', 'parasolid'],
           'gmcore': ['af5d89b9ce266cac5b45f2bf96e1324e87e54c6e2f568bd5b6a85c41122d39e4', 'base'],
           'aciskrnl': ['764e5633e6d502951788accfb8c34ed59430a4779a44d1775fd67f9aab8a654a', 'acis'],
           'msparalleladapt': ['8ae607112958f6b9d319736c71a6597cf99a8a59ceed733f2a939cb9cfa6dd67', 'paralleladapt'],
           'psint': ['f6c90b2fe87e690b2cba20f357d03c5962fed91541d6b79e01dc25cb8f01d1e0', 'parasolid'],
           'msadv': ['f18a8285d539cb07b00fde06fe970d958eceabf2a10182bcca6c8ad1c074c395', 'adv'],
        },
        'docs': {
           'MeshSim': ['f3c475072f270ff49ac2f6639ca1cddb0642889648cbea7df1a3f1b85f7cac36', 'base'],
           'GeomSimVoxel': ['9f4ee5a8204fee1d899cb912e0379f8be7a826e81ca0a0d8a670a4b804ca1276', 'voxel'],
           'MeshSimAdvanced': ['8c8bc3709238e600e8938c7c345588f8947d89eae98a228b0d0e3d46f5f4c0d9', 'adv'],
           'GeomSimDiscreteModeling': ['4e8e26a88e8a5ad396a637597a52f5973d8f77abc0a5b99fa737caf37226d6cc', 'discrete'],
           'GeomSimAdvanced': ['5efb38317d6be7862ce34024922ca372b30691a30af820474e2e26e4c3055278', 'advmodel'],
           'GeomSimParasolid': ['6851bdaf6d96e7b2335fce3394825e9876800f0aba0a42644758dc1bd06f60fe', 'parasolid'],
           'GeomSimImport': ['d931ecfc332460c825b473c0950c7ae8ff9f845e0d1565f85bfd7698da5e6d26', 'import'],
           'ParallelMeshSim': ['0f0d235b25a660271e401488e412220f574b341dadb827f7b82f0e93172b5cdb', 'parallelmesh'],
           'ParallelMeshSimAdapt': ['7964ebbd7e8d971ea85fc5260e44f7e876da5ad474dc67d8d6fc939bfa5ba454', 'paralleladapt'],
           'GeomSimAcis': ['dea82efbc4e3043ecda163be792ef295057e08be17654a7783ce7ca5e786f950', 'acis'],
           'MeshSimAdapt': ['ee4d5595572c1fe1a0d78bd9b85c774a55e994c48170450d6c5f34b05fcf2411', 'base'],
           'FieldSim': ['6b09b4ab278911d3e9229fd4cd8dc92ba188f151d42d9d7b96d542aad2af1fac', 'base'],
           'GeomSim': ['0673823d649998367c0e427055911eae971bb6e8c76625882e7a7901f4d18c44', 'base'],
           'GeomSimDiscrete': ['58dfd33fc5cdd2ab24e9084377943f28d5ba68b8c017b11b71cde64c5e4f2113', 'discrete'],
           'GeomSimAbstract': ['16248cd2a0d133029eb4b79d61397da008e4d5b5c3eaf0161a0a44148b0bc519', 'abstract'],
        }
    },
    {
        'version': '12.0-191027',
        'components': {
           'gmadv': ['1a133523062974c4d9acb1d52baa3893dc891482aebaaeb79a7dc907461d5dbc', 'advmodel'],
           'fdcore': ['c3a89093f811cb489698d203dbe68ca910e6c67ea75c0a7aba73dd369508b9ec', 'base'],
           'mscore': ['a2f043278d45d8729020b663c66c57960fcec33dafd3d90db55f0a9e32723bce', 'base'],
           'msparallelmesh': ['2f6fd47d3c5c2f1ece4634985a522ac599d3cee20ad8a4623f252cc75aa32c4c', 'parallelmesh'],
           'msparalleladapt': ['8d288730b1300215a32f3b21624bd2e0e2d8a684fe928459757fcec7e0aeb7d3', 'paralleladapt'],
           'gmabstract': ['3b608f21e6c11db5bb48e49f9cd7e9d88aeec4feadebd778529a5c9d506d08c6', 'abstract'],
           'gmimport': ['fc1626c7b1522b90eaa3926e1253b84d28440c7df8634decdedb79b5229be800', 'import'],
           'discrete': ['a15ead08138f0c59c7ee46cd0d348d4f26e1b021d2580a134cf2b84a7337bcf9', 'discrete'],
           'aciskrnl': ['8773f00e08d237052c877e79d1a869214f59891e812d70df938b2a5e5423a96f', 'acis'],
           'msadv': ['41bdb9555ab9feb0891f0832a49fc29777d40957473f315e1c33e1c0077cba7d', 'adv'],
           'psint': ['b040ab48833eb2a748f757e2de6929f3002aa98db459ba92bd9a88e443e5cb07', 'parasolid'],
           'gmvoxel': ['19fba83c9c7eac20d9613236530fbae652dc8edef35233214f0f92b81c91a877', 'voxel'],
           'msadapt': ['1a752adb6724c3328fffb26f1aebed007d3c2a5df725cd29aa0cf0fdfda1f39a', 'base'],
           'gmcore': ['ec95bae84b36644e6e04cf0a6b4e813a51990d0a30519176ebb8a05f681af7f2', 'base'],
           'pskrnl': ['7b7b4952513e06c8c23aa8f7c1748f5c199d9af70ea06c4a359412237ed8ac1d', 'parasolid'],
        },
        'docs': {
           'FieldSim': ['5109d91fe61ccdaf0af5aa869aea9c38ec98760746ec3983d100f870cbb1cb63', 'base'],
           'ParallelMeshSim': ['a1e6618a77022a9580beac4c698dd4b9aa70f617a27db9ce13ab1f2388475290', 'parallelmesh'],
           'GeomSimAcis': ['f0319b32eb417fa9b237575d9b2dc1c061848888c36fd4da97d97cdbb3cf19c3', 'acis'],
           'GeomSimAbstract': ['c44023e6944522057c47925db49089031c7de9b67938ca6a987e04fadfeda9b7', 'abstract'],
           'GeomSimDiscrete': ['ad648752fa7d2dc1ce234a612e28ce84eb1f064a1decadf17b42e9fe56967350', 'discrete'],
           'MeshSimAdapt': ['dcb7d6ec74c910b41b5ae707d9fd4664fcb3a0fdb2c876caaa28a6f1cf701024', 'base'],
           'MeshSim': ['e5a8cb300b1e13b9f2733bf8b738872ffb37d9df15836a6ab264483c10000696', 'base'],
           'GeomSimParasolid': ['2bf33cc5b3879716437d45fde0a02caaa165e37d248d05b4b00708e76573a15e', 'parasolid'],
           'GeomSimImport': ['5309433dcdce660e062412f070719eefcc6299764e9b0169533ff343c9c9c406', 'import'],
           'ParallelMeshSimAdapt': ['2e8e0ceede3107b85dba9536f3bbf5e6959793073a5147548cfb01ca568c8da2', 'paralleladapt'],
           'GeomSimDiscreteModeling': ['ff88ec234b890315cc36539e3f73f4f977dab94160860950e7b7ee0303c9b55e', 'discrete'],
           'GeomSim': ['62ae33372f999d5e62a1b7b161ddd7de04c055adc85cfd258e088c95b76d5fef', 'base'],
           'GeomSimVoxel': ['7a624ddaebd833077511acac3efd4b4c1dab09bd9feff40aba0813182eeb262f', 'voxel'],
           'GeomSimAdvanced': ['f0ab801ddf3d701a4ac3f8c47900cc858a4488eb0fe2f663504ba260cd270d20', 'advmodel'],
           'MeshSimAdvanced': ['bb532027e4fcc311a7c376383da010aed5ee133a9122b186a4e5c7d0cf1d976b', 'adv'],
        }
    }
    ]
    return releases


def simmetrix_makecomponenturl(name):
    """only supporting the linux libraries"""
    prefix = "file://{0}/".format(os.getcwd())
    suffix = "-" + "linux64.tgz"
    return prefix + name + suffix


def simmetrix_makedocurl(name):
    """doc zip files are not os/arch specific"""
    prefix = "file://{0}/".format(os.getcwd())
    suffix = '.zip'
    return prefix + name + suffix


def simmetrix_setkernelcmakeprefixpath(spec, path, env):
    if '+acis' in spec:
        env.append_path('CMAKE_PREFIX_PATH', join_path(path, 'acisKrnl'))
        env.append_path('LD_LIBRARY_PATH', join_path(path, 'acisKrnl'))
    if '+parasolid' in spec:
        env.append_path('CMAKE_PREFIX_PATH', join_path(path, 'psKrnl'))
        env.append_path('LD_LIBRARY_PATH', join_path(path, 'psKrnl'))


def simmetrix_resource(name, url, sha256, condition):
    # The tarballs/zips each have the same directory structure.  Because of
    # this, and the bug in spack described here:
    # https://github.com/spack/spack/pull/3553#issuecomment-391424244
    # , they cannot be expanded into the source root directory.
    # Once this is fixed the 'destination=name' argument can be removed.
    resource(
        name=name,
        url=url,
        sha256=sha256,
        destination=name,
        when=condition
    )


class SimmetrixSimmodsuite(Package):
    """Simmetrix' Simulation Modeling Suite is a set of component software
    toolkits that allow developers to easily implement geometry-based
    simulation applications.
    Each component of the Simulation Modeling Suite is designed to address
    specific capabilities:
    | MeshSim - automatic mesh generation
    | FieldSim - simulation data management
    | GeomSim - direct, untranslated access to geometry from a wide variety
    of sources
    """

    homepage = "http://www.simmetrix.com/products/SimulationModelingSuite/main.html"

    license_required = True
    license_vars     = ['SIM_LICENSE_FILE']

    variant('base', default=True, description='enable the base components')
    variant('crack', default=True, description='enable the meshsim crack components')
    variant('advmodel', default=False, description='enable advaced modeling')
    variant('abstract', default=False, description='enable abstract modeling')
    variant('voxel', default=False, description='enable voxel modeling')
    variant('discrete', default=False, description='enable discrete modeling')
    variant('acis', default=False, description='enable acis modeling')
    variant('parasolid', default=False, description='enable parasolid modeling')
    variant('opencascade', default=False, description='enable opencascade modeling')
    variant('granite', default=False, description='enable granite modeling')
    variant('import', default=False, description='enable import modeling')
    variant('adv', default=False, description='enable advanced meshing')
    variant('parallelmesh', default=False, description='enable parallel meshing')
    variant('paralleladapt', default=False, description='enable parallel adaptation')

    depends_on('mpi')

    oslib = 'x64_rhel7_gcc48'

    releases = simmodsuite_releases()
    for release in releases:
        # define the version using the mscore tarball
        sim_version = release['version']
        main_pkg_name = 'mscore'
        url = simmetrix_makecomponenturl(main_pkg_name)
        sha256 = release['components'][main_pkg_name][0]
        version(sim_version, sha256=sha256, url=url)
        # define resources for the other tarballs
        for name, atts in release['components'].items():
            # skip the tarball used for the version(...) call
            if name == 'mscore':
                continue
            sha256 = atts[0]
            feature = atts[1]
            url = simmetrix_makecomponenturl(name)
            condition = "@{0}+{1}".format(sim_version, feature)
            simmetrix_resource(name, url, sha256, condition)
        # define resources for the document zip files
        for name, atts in release['docs'].items():
            sha256 = atts[0]
            feature = atts[1]
            url = simmetrix_makedocurl(name)
            condition = "@{0}+{1}".format(sim_version, feature)
            simmetrix_resource(name, url, sha256, condition)

    def setup_dependent_build_environment(self, env, dependent_spec):
        archlib = join_path(prefix.lib, self.oslib)
        env.append_path('CMAKE_PREFIX_PATH', archlib)
        simmetrix_setkernelcmakeprefixpath(self.spec, archlib, env)

    def setup_run_environment(self, env):
        archlib = join_path(prefix.lib, self.oslib)
        env.append_path('CMAKE_PREFIX_PATH', archlib)
        simmetrix_setkernelcmakeprefixpath(self.spec, archlib, env)

    def install(self, spec, prefix):
        if not spec.satisfies('platform=linux'):
            raise InstallError('Only the linux platform is supported')
        source_path = self.stage.source_path
        for release in simmodsuite_releases():
            simversion = release['version']
            if simversion != spec.version.string:
                continue
            for name, atts in release['components'].items():
                feature = atts[1]
                if '+' + feature in spec:
                    if name == 'mscore':
                        install_tree(join_path(source_path, 'lib'), prefix.lib)
                        install_tree(
                            join_path(source_path, 'include'),
                            prefix.include)
                    else:
                        path = join_path(
                            source_path,
                            name,
                            self.version.string)
                        install_tree(path, prefix)
            for name, atts in release['docs'].items():
                feature = atts[1]
                if '+' + feature in spec:
                    path = join_path(
                        source_path,
                        name,
                        self.version.string)
                    install_tree(path, prefix)

        workdir = prefix.code.PartitionWrapper
        if '+parallelmesh' in spec:
            with working_dir(workdir):
                mpi_id = spec['mpi'].name + spec['mpi'].version.string
                # build the wrapper lib
                make("-f", "Makefile.custom",
                     "CC=%s" % spec['mpi'].mpicc,
                     "CXX=%s" % spec['mpi'].mpicxx,
                     "PARALLEL=%s" % mpi_id,
                     "PQUAL=-%s" % mpi_id,
                     "OPTFLAGS=-O2 -DNDEBUG " + self.compiler.cc_pic_flag)
                libname = 'libSimPartitionWrapper-' + mpi_id + '.a'
                wrapperlibpath = join_path(workdir, 'lib', libname)
                install(wrapperlibpath, join_path(prefix.lib, self.oslib))
