import sys

SysArg = int(sys.argv[1]) - 1

# DataSet 1
# Community1 = [50, 66, 67, 92, 112, 116, 126, 130, 146, 181, 192, 245, 266, 293, 295]
# Community2 = [2, 23, 33, 40, 77, 120, 123, 163, 190, 199, 205, 223, 229, 248, 273, 288, 298, 312, 315, 331]
# Community3 = [3, 6, 11, 15, 52, 82, 149, 268, 314, 353, 357, 367]
# Community4 = [4, 26, 58, 69, 103, 109, 142, 156, 157, 170, 201, 209, 243, 302, 306, 311, 370, 371]
# Community5 = [5, 13, 21, 53, 71, 133, 182, 183, 191, 210, 217, 231, 241, 250, 284, 294, 307, 319, 326, 329, 334]
# Community6 = [7, 18, 24, 37, 70, 80, 121, 177, 188, 256, 303, 320, 349, 360]
# Community7 = [8, 41, 124, 139, 173, 230, 240, 244, 258, 269, 296, 300, 322, 343, 345]
# Community8 = [9, 22, 54, 62, 64, 81, 89, 90, 99, 164, 252, 309]
# Community9 = [10, 44, 47, 63, 165, 167, 208, 260, 274, 317, 338]
# Community10 = [12, 29, 43, 55, 56, 94, 134, 219, 222, 239, 262, 263, 265, 308, 347]
# Community11 = [14, 42, 51, 57, 95, 96, 141, 166, 215, 218, 237, 289, 297, 299, 337, 363]
# Community12 = [16, 20, 39, 107, 128, 203, 226, 233, 254, 277, 287, 291, 373]
# Community13 = [17, 93, 125, 147, 168, 213, 236, 321, 372, 374]
# Community14 = [19, 25, 31, 76, 84, 111, 161, 175, 235, 253, 316, 330, 341, 376]
# Community15 = [27, 32, 45, 83, 108, 113, 118, 148, 150, 220, 238, 271, 281, 283, 304, 333, 340, 344, 346, 365]
# Community16 = [28, 72, 110, 138, 144, 145, 152, 158, 176, 180, 196, 202, 225, 227, 261, 290, 336, 339, 350, 356, 362, 377]
# Community17 = [30, 46, 60, 73, 74, 91, 178, 198, 212, 214, 242, 246, 255, 259, 352, 354, 358, 361]
# Community18 = [34, 59, 61, 65, 68, 100, 101, 143, 171, 186, 195, 216, 251, 292, 359, 368]
# Community19 = [38, 49, 79, 85, 87, 106, 114, 115, 117, 122, 132, 153, 154, 179, 197, 234, 257, 286, 305]
# Community20 = [48, 78, 135, 140, 193, 224, 276, 279, 328, 332, 348, 351, 366, 375]
# Community21 = [1, 35, 36, 86, 131, 151, 155, 174, 184, 185, 187, 207, 211, 267, 278, 301, 323, 324, 355, 378]
# Community22 = [75, 97, 102, 119, 129, 137, 169, 172, 189, 232, 247, 272, 282, 285, 310, 318, 325, 342, 369]
# Community23 = [88, 98, 105, 127, 162, 249, 275, 280, 327, 364]
# Community24 = [104, 136, 159, 160, 194, 200, 204, 206, 221, 228, 264, 270, 313, 335]

# Communities1 = [Community1, Community2, Community3, Community4, Community5, Community6, Community7, Community8,
#               Community9, Community10, Community11, Community12, Community13, Community14, Community15, Community16,
#               Community17, Community18, Community19, Community20, Community21, Community22, Community23, Community24]

# DataSet 2
Community1 = ["V1", "V2", "V15", "V106", "V107", "V136", "V153", "V155", "V159", "V173", "V257", "V303", "V341", "V451",
              "V483", "V526", "V549", "V554", "V556", "V560", "V561", "V655", "V677"]
Community2 = ["V3", "V51", "V63", "V319", "V376", "V377", "V378", "V380", "V521", "V576", "V577", "V578", "V579",
              "V580", "V581", "V582", "V583", "V584", "V586", "V587", "V588", "V622", "V646", "V648", "V671", "V673",
              "V684", "V740", "V742", "V746", "V765", "V797"]
Community3 = ["V4", "V7", "V8", "V54", "V100", "V101", "V132", "V140", "V142", "V146", "V147", "V148", "V149", "V150",
              "V161", "V167", "V184", "V270", "V275", "V389", "V423", "V427", "V491", "V611", "V702", "V705", "V805",
              "V830"]
Community4 = ["V5", "V10", "V108", "V119", "V211", "V288", "V296", "V304", "V307", "V328", "V336", "V339", "V354",
              "V372", "V397", "V403", "V429", "V506", "V718", "V728", "V752"]
Community5 = ["V6", "V11", "V92", "V93", "V103", "V109", "V117", "V121", "V122", "V124", "V131", "V205", "V206",
              "V208", "V248", "V256", "V265", "V357", "V366", "V394", "V399", "V428", "V430", "V432", "V505", "V507",
              "V527", "V753"]
Community6 = ["V9", "V17", "V207", "V212", "V268", "V269", "V301", "V311", "V313", "V315", "V318", "V321", "V323",
              "V324", "V325", "V326", "V327", "V337", "V340", "V401", "V450", "V465", "V469", "V627", "V639", "V642",
              "V704", "V743", "V747"]
Community7 = ["V12", "V52", "V69", "V75", "V83", "V387", "V393", "V400", "V405", "V416", "V436", "V486", "V487",
              "V534", "V800", "V803", "V810"]
Community8 = ["V13", "V47", "V60", "V70", "V76", "V84", "V177", "V343", "V363", "V368", "V390", "V391", "V402", "V417",
              "V443", "V445", "V447", "V448", "V449", "V453", "V460", "V470", "V471", "V472", "V473", "V474", "V515",
              "V796"]
Community9 = ["V14", "V16", "V25", "V32", "V35", "V44", "V56", "V65", "V78", "V80", "V409", "V411", "V501", "V517",
              "V518", "V519", "V520", "V523", "V539", "V754", "V760", "V761", "V769", "V771", "V774", "V775", "V776",
              "V777", "V778", "V807"]
Community10 = ["V18", "V30", "V31", "V68", "V116", "V152", "V292", "V297", "V300", "V434", "V438", "V492", "V493",
               "V531", "V664", "V665", "V666", "V686", "V726", "V727", "V814", "V820", "V821", "V822", "V833"]
Community11 = ["V19", "V20", "V34", "V45", "V57", "V66", "V72", "V79", "V90", "V91", "V144", "V245", "V420", "V435",
               "V490", "V528", "V544", "V570", "V628", "V629", "V631", "V632", "V633", "V732", "V736", "V823", "V824",
               "V826"]
Community12 = ["V21", "V27", "V37", "V40", "V42", "V61", "V192", "V239", "V392", "V410", "V455", "V456", "V457",
               "V459", "V461", "V462", "V467", "V475", "V476", "V477", "V478", "V489", "V516", "V540", "V755", "V762",
               "V764", "V766", "V768", "V772", "V773", "V809", "V811"]
Community13 = ["V22", "V36", "V38", "V46", "V59", "V67", "V74", "V82", "V130", "V176", "V398", "V412", "V415", "V431",
               "V439", "V488", "V533", "V781", "V782", "V783", "V789", "V790", "V792", "V793", "V795"]
Community14 = ["V23", "V24", "V29", "V33", "V39", "V55", "V64", "V73", "V81", "V87", "V104", "V113", "V114", "V193",
               "V408", "V419", "V497", "V522", "V661", "V662", "V663", "V756", "V758", "V798", "V799", "V802", "V806",
               "V812", "V815"]
Community15 = ["V26", "V115", "V171", "V217", "V223", "V225", "V226", "V227", "V228", "V229", "V230", "V231", "V233",
               "V237", "V418", "V495", "V496", "V498", "V500", "V509", "V511", "V512", "V513", "V514", "V537", "V538",
               "V602", "V636", "V757", "V770", "V801", "V808"]
Community16 = ["V28", "V49", "V86", "V88", "V89", "V123", "V386", "V388", "V406", "V440", "V444", "V452", "V463",
               "V468", "V480", "V499", "V502", "V503", "V504", "V508", "V524", "V767", "V816", "V817", "V818", "V819"]
Community17 = ["V41", "V50", "V112", "V204", "V240", "V260", "V264", "V298", "V331", "V332", "V333", "V351", "V360",
               "V361", "V532", "V541", "V703", "V734", "V794", "V825"]
Community18 = ["V43", "V48", "V62", "V71", "V77", "V85", "V111", "V118", "V168", "V170", "V189", "V191", "V209",
               "V210", "V213", "V214", "V215", "V216", "V218", "V219", "V220", "V221", "V222", "V224", "V232", "V234",
               "V235", "V236", "V238", "V407", "V458"]
Community19 = ["V53", "V282", "V373", "V375", "V379", "V381", "V383", "V384", "V396", "V413", "V454", "V485", "V535",
               "V574", "V575", "V626", "V644", "V645", "V647", "V649", "V650", "V659", "V660", "V668", "V669", "V670",
               "V672", "V674", "V682", "V683", "V685", "V692", "V693", "V710", "V804"]
Community20 = ["V58", "V110", "V143", "V165", "V166", "V259", "V267", "V284", "V308", "V309", "V342", "V345", "V346",
               "V347", "V348", "V352", "V369", "V385", "V737", "V739", "V741", "V745", "V763"]
Community21 = ["V94", "V125", "V126", "V127", "V128", "V129", "V169", "V174", "V175", "V187", "V243", "V274", "V276",
               "V277", "V286", "V312", "V317", "V329", "V350", "V353", "V421", "V484", "V542", "V697", "V712", "V714",
               "V715", "V717", "V719", "V720", "V723", "V730", "V731", "V748", "V785", "V828"]
Community22 = ["V95", "V137", "V156", "V158", "V164", "V180", "V181", "V202", "V203", "V424", "V546", "V547", "V548",
               "V550", "V551", "V552", "V553", "V555", "V557", "V558", "V559", "V562", "V617", "V680", "V689", "V750",
               "V827"]
Community23 = ["V96", "V138", "V242", "V482", "V525", "V530", "V589", "V590", "V592", "V593", "V594", "V596", "V598",
               "V600", "V601", "V604", "V606", "V608", "V614", "V675", "V696", "V735"]
Community24 = ["V97", "V98", "V102", "V120", "V246", "V247", "V251", "V252", "V254", "V255", "V262", "V263", "V272",
               "V344", "V359", "V364", "V365", "V437", "V441", "V442", "V446", "V464", "V466", "V479", "V481", "V494"]
Community25 = ["V99", "V105", "V134", "V179", "V182", "V183", "V185", "V186", "V188", "V190", "V194", "V195", "V196",
               "V197", "V198", "V199", "V200", "V201", "V334", "V404", "V510", "V694", "V725", "V759", "V788", "V813"]
Community26 = ["V133", "V135", "V139", "V151", "V154", "V157", "V160", "V250", "V253", "V261", "V266", "V271", "V273",
               "V367", "V425", "V426", "V433", "V563", "V567", "V572", "V613", "V637", "V640", "V643", "V652", "V658",
               "V667", "V681", "V687", "V688", "V691", "V701", "V738", "V749", "V831", "V832"]
Community27 = ["V141", "V241", "V249", "V294", "V299", "V302", "V306", "V310", "V316", "V320", "V330", "V566", "V621",
               "V657", "V698", "V700", "V707", "V713", "V716", "V721", "V722", "V724", "V729", "V779"]
Community28 = ["V145", "V279", "V283", "V289", "V290", "V291", "V293", "V314", "V358", "V395", "V414", "V529", "V564",
               "V610", "V612", "V615", "V619", "V620", "V623", "V630", "V634", "V656", "V690", "V706", "V708", "V751"]
Community29 = ["V162", "V163", "V172", "V178", "V244", "V258", "V374", "V422", "V536", "V543", "V565", "V568", "V571",
               "V573", "V585", "V624", "V625", "V651", "V676", "V711", "V829"]
Community30 = ["V278", "V280", "V281", "V285", "V287", "V295", "V305", "V322", "V335", "V338", "V349", "V355", "V356",
               "V362", "V370", "V371", "V382", "V545", "V709", "V744", "V780", "V784", "V786", "V787", "V791"]
Community31 = ["V569", "V591", "V595", "V597", "V599", "V603", "V605", "V607", "V609", "V616", "V618", "V635", "V638",
               "V641", "V653", "V654", "V678", "V679", "V695", "V699", "V733"]

Communities2 = [Community1, Community2, Community3, Community4, Community5, Community6, Community7, Community8,
                Community9, Community10, Community11, Community12, Community13, Community14, Community15, Community16,
                Community17, Community18, Community19, Community20, Community21, Community22, Community23, Community24,
                Community25, Community26, Community27, Community28, Community29, Community30, Community31]

# DataSet 3
Community1 = ["V1", "V8", "V23", "V31", "V38", "V442", "V454", "V465", "V478", "V491", "V503", "V515", "V528", "V556"]
Community2 = ["V2", "V9", "V16", "V24", "V32", "V39", "V57", "V179", "V214", "V235", "V692", "V727", "V739"]
Community3 = ["V3", "V10", "V17", "V25", "V33", "V40", "V50", "V58", "V66", "V257", "V493", "V505", "V558", "V574",
              "V583", "V591", "V603", "V615", "V621", "V683", "V693", "V713"]
Community4 = ["V4", "V11", "V27", "V34", "V52", "V68", "V89", "V537", "V569", "V579", "V587", "V594", "V618", "V651",
              "V741"]
Community5 = ["V5", "V15", "V20", "V28", "V35", "V43", "V153", "V160", "V205", "V254", "V280", "V339", "V451", "V488",
              "V538", "V547", "V576", "V605", "V652", "V695", "V699", "V730"]
Community6 = ["V6", "V29", "V36", "V74", "V123", "V147", "V151", "V152", "V201", "V283", "V410", "V512", "V523", "V550",
              "V655", "V665", "V678", "V696", "V717", "V731", "V734", "V742"]
Community7 = ["V7", "V22", "V30", "V37", "V45", "V54", "V62", "V91", "V167", "V476", "V501", "V513", "V563", "V581",
              "V612", "V654", "V666", "V679", "V686", "V697", "V705", "V716", "V733", "V743"]
Community8 = ["V12", "V53", "V69", "V86", "V87", "V88", "V99", "V259", "V261", "V281", "V305", "V340", "V359", "V390",
              "V408", "V489", "V500", "V526", "V562", "V570", "V586", "V595", "V611", "V631", "V685"]
Community9 = ["V13", "V116", "V124", "V148", "V231", "V306", "V341", "V360", "V453", "V464", "V490", "V540", "V554",
              "V626", "V636"]
Community10 = ["V14", "V47", "V48", "V56", "V64", "V71", "V93", "V207", "V300", "V354", "V373", "V403", "V431", "V541"]
Community11 = ["V18", "V51", "V84", "V296", "V310", "V315", "V330", "V331", "V349", "V396", "V399", "V418", "V425",
               "V445", "V457", "V575", "V598", "V622"]
Community12 = ["V19", "V60", "V97", "V114", "V122", "V182", "V200", "V229", "V249", "V474", "V486", "V499", "V624",
               "V677", "V694", "V703", "V714", "V729"]
Community13 = ["V21", "V44", "V61", "V90", "V166", "V439", "V452", "V475", "V539", "V553", "V560", "V568", "V578",
               "V580", "V585", "V588", "V593", "V600", "V609", "V617", "V623", "V625"]
Community14 = ["V26", "V41", "V59", "V109", "V157", "V190", "V223", "V285", "V308", "V412", "V532", "V559", "V709"]
Community15 = ["V42", "V146", "V165", "V260", "V267", "V279", "V304", "V326", "V338", "V358", "V377", "V389", "V407",
               "V438", "V450", "V462", "V511", "V525", "V552", "V561", "V610", "V630", "V664"]
Community16 = ["V46", "V63", "V92", "V155", "V255", "V263", "V299", "V372", "V514", "V551", "V555", "V571", "V645",
               "V661", "V674", "V725"]
Community17 = ["V49", "V72", "V107", "V443", "V467", "V492", "V504", "V557", "V590", "V601", "V614", "V632", "V662"]
Community18 = ["V55", "V187", "V206", "V353", "V441", "V477", "V502", "V613", "V681", "V691", "V700", "V711", "V738"]
Community19 = ["V65", "V94", "V119", "V143", "V162", "V197", "V225", "V455", "V564", "V648", "V675", "V682", "V701",
               "V712"]
Community20 = ["V67", "V239", "V343", "V362", "V481", "V494", "V506", "V584", "V604", "V616", "V690", "V722", "V737"]
Community21 = ["V70", "V184", "V202", "V219", "V251", "V269", "V282", "V328", "V379", "V391", "V409", "V440", "V527"]
Community22 = ["V73", "V75", "V76", "V77", "V78", "V79", "V80", "V81", "V82", "V83", "V85", "V487", "V510", "V656"]
Community23 = ["V95", "V108", "V120", "V144", "V163", "V180", "V198", "V215", "V227", "V237", "V265", "V277", "V302",
               "V324", "V336", "V356", "V375", "V386", "V405"]
Community24 = ["V96", "V113", "V121", "V145", "V164", "V181", "V199", "V216", "V228", "V248", "V266", "V278", "V376",
               "V406", "V466", "V646", "V647", "V653", "V657", "V718", "V726", "V732", "V735"]
Community25 = ["V98", "V115", "V183", "V217", "V218", "V230", "V250", "V258", "V268", "V327", "V378", "V388", "V463",
               "V599", "V619", "V634", "V635", "V650", "V684", "V704", "V715"]
Community26 = ["V100", "V101", "V117", "V118", "V125", "V126", "V149", "V150", "V168", "V169", "V185", "V186", "V203",
               "V204", "V220", "V221", "V232", "V233", "V252", "V253"]
Community27 = ["V102", "V106", "V154", "V156", "V170", "V188", "V208", "V234", "V262", "V284", "V307", "V329", "V342",
               "V361", "V392", "V411", "V698"]
Community28 = ["V103", "V129", "V137", "V140", "V159", "V173", "V174", "V189", "V191", "V210", "V226", "V240", "V246",
               "V272"]
Community29 = ["V104", "V161", "V172", "V275", "V295", "V314", "V322", "V363", "V366", "V367", "V370", "V421"]
Community30 = ["V105", "V110", "V111", "V139", "V192", "V193", "V212", "V213", "V236", "V241", "V243", "V244", "V245",
               "V333"]
Community31 = ["V112", "V128", "V131", "V133", "V171", "V176", "V178", "V196", "V209", "V211", "V271", "V381", "V393",
               "V469", "V567", "V592", "V629", "V748"]
Community32 = ["V127", "V222", "V270", "V380", "V518", "V660", "V672", "V680", "V689", "V708", "V721", "V736"]
Community33 = ["V130", "V135", "V136", "V158", "V194", "V238", "V242", "V247", "V287", "V294", "V298", "V309", "V332",
               "V347", "V352", "V383", "V384", "V397", "V429"]
Community34 = ["V132", "V134", "V138", "V141", "V142", "V175", "V177", "V195", "V224", "V290", "V334", "V365"]
Community35 = ["V256", "V264", "V276", "V301", "V323", "V335", "V355", "V374", "V385", "V404", "V516", "V529", "V542",
               "V572", "V596", "V620", "V627"]
Community36 = ["V273", "V293", "V311", "V317", "V348", "V351", "V382", "V398", "V402", "V414", "V415"]
Community37 = ["V274", "V286", "V288", "V289", "V292", "V312", "V319", "V320", "V321", "V395", "V400", "V416", "V424",
               "V428"]
Community38 = ["V291", "V297", "V313", "V345", "V350", "V371", "V394", "V413", "V419", "V422", "V426", "V427", "V430"]
Community39 = ["V303", "V325", "V337", "V357", "V387", "V433", "V444", "V456", "V468", "V480", "V517", "V531", "V543",
               "V566", "V597", "V628", "V633", "V649", "V663", "V676", "V702", "V728", "V740"]
Community40 = ["V316", "V318", "V344", "V346", "V364", "V368", "V369", "V401", "V417", "V420", "V423"]
Community41 = ["V432", "V479", "V530", "V565", "V573", "V582", "V602", "V637", "V638", "V667", "V671", "V706", "V723"]
Community42 = ["V434", "V435", "V446", "V447", "V458", "V459", "V470", "V471", "V482", "V483", "V495", "V496", "V507",
               "V508", "V519", "V520", "V533", "V534", "V544", "V545"]
Community43 = ["V436", "V460", "V472", "V484", "V497", "V509", "V521", "V524", "V535", "V546", "V577", "V589", "V606",
               "V607", "V608", "V673", "V710", "V724"]
Community44 = ["V437", "V448", "V449", "V461", "V473", "V485", "V498", "V522", "V536", "V548", "V549"]
Community45 = ["V639", "V640", "V641", "V642", "V643", "V644", "V658", "V659", "V668", "V669", "V670", "V687", "V688",
               "V707", "V719", "V720", "V744", "V745", "V746", "V747"]

Communities3 = [Community1, Community2, Community3, Community4, Community5, Community6, Community7, Community8,
                Community9, Community10, Community11, Community12, Community13, Community14, Community15, Community16,
                Community17, Community18, Community19, Community20, Community21, Community22, Community23, Community24,
                Community25, Community26, Community27, Community28, Community29, Community30, Community31, Community32,
                Community33, Community34, Community35, Community36, Community37, Community38, Community39, Community40,
                Community41, Community42, Community43, Community44, Community45]


def LCSubStr(X, Y):
    m = len(X)
    n = len(Y)
    # Create a table to store lengths of longest common suffixes of substrings.
    # Note that LCSuff[i][j] contains the length of longest common suffix of
    # X[0...i-1] and Y[0...j-1]. The first row and first column entries have no
    # logical meaning, they are used only for simplicity of the program.

    # LCSuff is the table with zero value initially in each cell
    LCSuff = [[0 for k in range(n)] for l in range(m)]

    # To store the length of longest common substring
    result = 0
    last_index1 = 0

    # Following steps to build LCSuff[m+1][n+1] in bottom up fashion
    for i in range(m):
        for j in range(n):
            if (i == 0 or j == 0):
                LCSuff[i][j] = 0
            elif (X[i - 1] == Y[j - 1]):
                LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1
                result = max(result, LCSuff[i][j])
                if (result == LCSuff[i][j]):
                    last_index1 = i
            else:
                LCSuff[i][j] = 0

    Ind1 = last_index1 - result
    sstr = ""

    for k in range(Ind1, last_index1):
        sstr = str(sstr) + str(X[k]) + " "

    return len(sstr), len(sstr)


def lcs(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0 for x in range(0, n + 1)] for y in range(0, m + 1)]

    # Following steps build L[m+1][n+1] in bottom up fashion. Note
    # that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]
    for i in range(m+1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
                # print("LCSL: "+str(L[i][j]))
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
                # print("LCSL: " + str(L[i][j]))

    # Following code is used to print LCS
    # print(str(L[m-1][n-1]) + " : "+str(L[m-1][n])+ " : "+str(L[m][n-1])+" : "+str(L[m][n]))

    index = L[m][n]
    OutIndex = index

    # Create a character array to store the lcs string
    lcs = [""] * (index + 1)
    lcs[index] = ""

    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs[]
    i = m
    j = n
    while i > 0 and j > 0:

        # If current character in X[] and Y are same, then
        # current character is part of LCS
        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1

        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    outputLCS = " ".join(lcs)


    return len(outputLCS), len(outputLCS)


def RecursiveLCSSeq(inpStrList):
    LCSeqList = list()
    for i in range(0, len(inpStrList) - 1):
        j = i + 1
        sseq = lcs(inpStrList[i], inpStrList[j])
        #print("SSEQ: " + sseq)
        LCSeqList.append(sseq)

    if len(LCSeqList) == 1:
        print("LCSSeqDONE")
        return LCSeqList[0]
    else:
        RecursiveLCSSeq(LCSeqList)


def RecursiveLCSStr(inpStrList):
    LCStrList = list()
    for i in range(0, len(inpStrList) - 1):
        j = i + 1
        sstrLen, ind1 = LCSubStr(inpStrList[i], inpStrList[j])
        Ind1 = ind1 - (sstrLen)
        sstr = ""

        for k in range(Ind1, ind1):
            sstr = str(sstr) + str(inpStrList[i][k]) + " "
        LCStrList.append(sstr)

    if len(LCStrList) == 1:
        print("LCSStrDONE")
        return LCStrList[0]
    else:
        RecursiveLCSStr(LCStrList)


def states_to_list(file1):
    filename = file1[1:]
    #print("FILENUM: "+filename)
    Str1 = list()

    # File Directories of the files on the cluster vs home machine
    inpFile1 = open("/Users/jeffmills/PycharmProjects/EfficientKL_V1.0/LinuxDataSet/Trace" + filename + ".txt", "r")
    #inpFile1 = open("/home/millsjw2/GhoshMillsWork/DataFiles/Trace" + filename + ".txt", "r")
    for line in inpFile1:
        ints = line.split()
        for int in ints:
            Str1.append(int)
    return Str1


##Main DRIVER:
CurrComm = Communities2[SysArg]

FileStrList = list()
for file in CurrComm:
    FileStr = states_to_list(file)
    FileStrList.append(FileStr)
#print("FSLLEN: "+str(len(FileStrList)))

LCSSeqAdj = [[0 for x in range(len(FileStrList))] for y in range(len(FileStrList))]
LCSStrAdj = [[0 for x in range(len(FileStrList))] for y in range(len(FileStrList))]

for i in range(0, len(FileStrList)):
    for j in range(0, len(FileStrList)):
        if j > i :
            LCSSeqAdj[i][j], LCSSeqAdj[j][i] = lcs(FileStrList[i], FileStrList[j])
            LCSStrAdj[i][j], LCSStrAdj[j][i] = LCSubStr(FileStrList[i], FileStrList[j])


CommNum = SysArg+1

outFile = "D2_Community_" + str(CommNum)+ "_LCSeq.txt"
with open(outFile, "w") as out:
    for i in range(0, len(FileStrList)):
        for j in range(0, len(FileStrList)):
            out.write(str(LCSSeqAdj[i][j]) + ",")
        out.write("\n")
out.close()

outFile = "D2_Community_" + str(CommNum) + "_LCStr.txt"
with open(outFile, "w") as out:
    for i in range(0, len(FileStrList)):
        for j in range(0, len(FileStrList)):
            out.write(str(LCSStrAdj[i][j]) + ",")
        out.write("\n")
out.close()

