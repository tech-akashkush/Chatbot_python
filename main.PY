


import re
import long_responses as long
def message_probability(user_message, recognised_words, single_response=False, required_words=[], g_link=False, fb_link=False, yt_link=False, all_abmu_no=False, all_gov_schemes=False, all_hospital_no=False, all_chemist_no=False, women_schemes=False, women_helpline=False, ch_greater=False, d_chemmist=False, d_amb=False, up_amb=False):
    message_certainty = 0
    has_required_words = True
# Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words: 
            message_certainty += 1
# Calculates the percent of recognised words in a user message 
    percentage = float(message_certainty) / float(len(recognised_words))
# Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break



    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0
    

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[], g_link=False, yt_link=False, fb_link=False, all_abmu_no=False, all_gov_schemes=False, all_hospital_no=False, all_chemist_no=False, women_schemes=False, women_helpline=False, ch_greater=False, d_chemmist=False, d_amb=False, up_amb=False):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words, g_link, yt_link, fb_link, all_abmu_no, all_gov_schemes, all_hospital_no, all_chemist_no, women_schemes, women_helpline, ch_greater, d_chemmist, d_amb, up_amb)


    #Response------------------------------------------

    response('Hello!', ['hello', 'hi', 'sup', 'hey', 'heyo'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how']) 
    response ('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])

    response('www.facebook.com',['facebook','facebook link','give me facebook link'  ] , fb_link=True)
    response('www.youtube.com',['youtube','youtube link','give me youtube link'  ] , yt_link=True)
    response('www.google.com',['google','google link','give me google link' ] , g_link=True)



    # all ambulance
     
    response('\n1: Hospital Name: All India Institute of Medical Science (AIIMS)\nAddress: Ansari Nagar, New Delhi - 110029\nPhone no. 011-26588776\n2: Hospital Name: Centralized Accident Trauma Service (CATS)\nAddress: Cats Head Quarter, Bela Road, Near Vijay Gate, Delhi-110054\n Phone no. 102, 1099\n3: Hospital Name: Escort Hospital\n Address: 141, A, Sarai Jullena, New Friends Colony, New Delhi, Delhi 110049\n Phone no. 011- 26825000\n4: Hospital Name: Moolchand Hospital\n Address: Batra Hospital\n Phone no. 011- 42000000\n5: Hospital Name: Batra Hospital\n Address:  1, Tughlakabad Institutional Area, M.B. Road, New Delhi, 110062\n Phone no. 011- 26083747\n6: Hospital Name: Rajiv Gandhi Cancer Institute\n Address: Sir Chotu Ram Marg, Sector - 5, Rohini Industrial Area, Rohini, New Delhi - 110085\n Phone no. 011- 27051011\n7: Hospital Name: National Heart Institute\n Address: 49 50, Community Center East of Kailash, Delhi, Delhi - 110065.\n Phone no. 011- 26441293\n8: Hospital Name: Sir Ganga Ram Hospital\n Address: 49 50, Community Center East of Kailash, Delhi, Delhi - 110065.\n Phone no. 011- 25750000, 25757575\n9: Hospital Name: Vidyasagar Institute of Mental Health and NeuroSciences (VIMHANS)\n Address: Institutional Area, Nehru Nagar, New Delhi-110065\n Phone no.  011- 26924302\n10: Hospital Name: MP Heart Centre\n Address: W-33, Greater Kailash 1. Landmark:- Near Police Station, Delhi\n Phone no. 011- 6413436\n11: Hospital Name: Anand Hospital\n Address: B-52, New Krishna Park, Dhali Piao, Vikaspuri, Delhi - 110018\n Phone no. 011- 2224126\n12: Hospital Name: Holy Angles Hospital\n Address: Plot B, Community Center, Basant Lok Landmark: Behind Vasant Continental Hotel & Near Priya Cinema Vasant, Delhi\n13: GM Modi Hospital\n Address: Press Enclave Road, Saket Malviya Nagar, New Delhi - 110017, Delhi\n Phone no. 011- 6852112\n14: Hospital Name: PS Funeral & Ambulance Services Private Limited\n Address: SOL Technologies Solutions, First Floor, 273, opp. Ansal Plaza, South Extension, Masjid Moth Village, New Delhi, Delhi 110049\n Phone no. 09350016581, 08373903017\n15: Hospital Name: Max Emergency Ambulance\n Address: Bensups Hospital, Sector-12, Dwarka, New Delhi-110075\n Phone no. 011- 40554055\n16: Hospital Name: Goodmans Rescue Ambulance Service\n Address: Goodmans Rescue Ambulance Service\n Phone no. 011- 29231665, 46566890   ',['all ambulance number','all ambulance','numbers of ambulance','ambulance' ] , all_abmu_no=False)
    #response('\nHosipatal Name: All India Institute of Medical Science (AIIMS)\nAddress: Ansari Nagar, New Delhi - 110029\nPhone no. 011-26588776',['all ambulance number','all ambulance','numbers of ambulance','ambulance' ] , all_abmu_no=False)
  #  response('',['all ambulance number','all ambulance','numbers of ambulance','ambulance' ] , all_abmu_no=False)
    


    #all gov schemes

    response('\n1: Schemes Name: Pradhan Mantri Kisan Samman Nidhi(PM-KISAN)\n2: Schemes Name: Pradhan Mantri Krishi Sinchai Yojana(PMKSY)\n3: Pradhan Mantri Fasal Bima Yojana(PMFBY)\n4: Deen Dayal Upadhyaya Grameen Kaushalya Yojana(DDU-GKY)\n5: Pradhan Mantri Gramin Awas Yojana (PMAY-G)\n6: Pradhan Mantri Jan Dhan Yojana (PMJDYv)\n7: Pradhan Mantri Jan Dhan Yojana (PMJDY)\n8: Pradhan Mantri Matru Vandana Yojana (PMMVY)\n9: Beti Bachao Beti Padhao (BBBP)\n10: Pradhan Mantri Kaushal Vikas Yojana (PMKVY)\n11: Ayushman Bharat Yojana (AB-PMJAY)\n12: Arogya Sanjeevani Health Insurance Scheme\n13: Jan Aushadhi Scheme\n14: Pradhan Mantri Ujjwala Yojana (PMUY)\n15: Pradhan Mantri Suraksha Bima Yojana (PMSBY)\n16: Pradhan Mantri Jeevan Jyoti Bima Yojana (PMJJBY)\n17: Indira Gandhi National Old Age Pension Scheme (IGNOAPS)\n18: Pradhan Mantri Shram Yogi Maan-Dhan (PM-SYM)\n16: Pradhan Mantri Awas Yojana (PMAY-U) ',['all government schemes','all private schemes','all schemes','numbers of government schemes','schemes' ] , all_gov_schemes=False)





    # ALL HOSPITALS

    response('\n1: Lok Nayak Hospital \nAddress: metro Station Central, Jawaharlal Nehru Marg, near Delhi Gate, New Delhi, Delhi 110002 \n Phone: 011 2354 3807\n2: Aruna Asaf Ali Govt Hospital Addres: 5, Rajpur Rd, Police Lines, Civil Lines, New Delhi, Delhi, 110054 Phone: 011 2396 5532\n3: Pt. Madan Mohan Malaviya Hospital Address: Khirki Extension, Malviya Nagar, New Delhi, Delhi 110017\n Phone: 011 2668 9999 \n4:Lal Bahadur Shastri Hospital \n Address: 384, Indra Camp, near Lal Bahadur Shashtri hospital emergency gate, Khichripur, Kalyan Puri, Delhi, 110091 \nPhone: 1800 11 2526 \n5.Dr. N.C. Joshi Memorial Hospital \n Address: M52X+PPG, Joshi Path, near Ajmal Khan Park, Block A, Karol Bagh, New Delhi, Delhi, 110005 \n Phone: 011 2362 2498 \n6. Ambedkar Nagar Hospital \n Address: K-582, Maharishi Balmiki Rd, Dr.Ambedkar Nagar, Block K, Dakshin Puri Extension, Dakshinpuri, New Delhi, Delhi 110062 \n Phone: 095995 95202\n7. Deen Dayal Upadhyay Hospital \n Adrress: 4H6+6W3, Shaheed Mangal Pandey Marg, Nanak Pura,Hari Nagar, New Delhi, Delhi, 110064 \n Phone: 011 2549 4402 \n8. Charak Palika Hospital \n Address: C 7 Ln, Moti Bagh 1, Block F, Moti Bagh, New Delhi, Delhi 110021 \n Phone: 011 2611 7879 \n9. Deep Chand Bandhu Hospital \n Address: Ashok Vihar Rd, Kokiwala Bagh, Phase 4, Ashok Vihar IV, Ashok Vihar, New Delhi, Delhi, 110052 \n Phone: 079050 71813 \n 10.Apollo Spectra Hospitals \n Adress: Metro Pillar No. 77, Block No. 34, Plot No. 3, Pusa Rd, opposite Bal Bharati Public School, Block 18 A, WEA, Karol Bagh, New Delhi, Delhi, 110005 \n Phone: 084484 40991 \n11. Primus Super Speciality Hospital \n Address: Chandragupta Marg, Opp Russian Embassy, Chanakyapuri, New Delhi, Delhi 110021\n Phone: 011 6620 6630 \n12.Jeewan Mala Hospital \n Address: 67/1 New Rohtak Road, Guru Gobind Singh Marg, Karol Bagh, New Delhi, Delhi 110005 \n Phone: 011 4777 4151 \n13.Holy Angels Hospital \n Address: Plot B Community Center Vasant Lok near Vasant Vihar Metro station, behind Jaypee Continental Hotel, New Delhi, Delhi 110057 \n Phone: 011 4335 7700 \n14. Sanjeevan Hospital \n Address: 24, Ansari Rd, Daryaganj, New Delhi, Delhi, 110002 Phone: 011 4577 0000 \n15. Lotus Hospital	 WZ-409-A, Janak Park, Pocket 408, Hari Nagar, New Delhi, Delhi, 110064	\n Phone: 011 2575 0000 \n16. Northern Railway Central Hospital \n Adress: Basant Lane, Aram Bagh, Connaught Place, Paharganj, New Delhi, Delhi 110055 \n 	Phone: 011 2336 4227 \n17.Sardar Vallabh Bhai Patel Hospital \n Address: East Patel Nagar, Patel Nagar, New Delhi, Delhi, 110008 \n Phone: 011 2588 5944',['all hospital number','all private hospital','numbers of hospital','government hospital' ] , all_hospital_no=False)

    
    
    
    # all chemist 
    
    response('\n1: Chemist Name:Pradhanmantri Bhartiya Janaushadhi Kendra \nAddress: X, X-421, 421, near Sanjay Gandhi Hospital, Mangolpuri, New Delhi, Delhi 110083 \nPhone no. 079825 71874 \n2: Chemist Name:South City Pharmacy \nAddress:Shop no. 1, opposite Southcity Arcade, South City I, Gurugram, Haryana 122002 \nPhone no.08800765856 \n3: Chemist Name:Dev Chemist \nAddress:A 6, Nanda Road, Gali Number 1, near Government school, Mool Chand Nagar, Adarsh Nagar, Delhi, 110033 \nPhone no.09990013689 \n4 Chemist Name:Narayani Chemist Pvt Ltd \nAddress:Shop No 13, 14, Block G, South City I, Arcade, Sukhrali, Gurugram, Haryana 122001 \nPhone no.098107 29004 \n5 Chemist Name:Jan Aushadhi Kendra \nAddress:Shop No 14, DDA Market, Block LU, Uttari Pitampura, Pitampura, Delhi, 110034 \nPhone no.098712 47737 \n5: Chemist Name:Ajay Medical Store \nAddress:Shop No. 5, near Max Hospital Atta Market, Noida Sector 18, Atta Market, Pocket E, Sector 27, Noida, Uttar Pradesh 201301 \nPhone no.099119 66355 \n6 Chemist Name:Apollo Pharmacy Shalimar Bagh \nAddress:Shop No 1, Plot No 5, Ground Floor, Mahadevi Chamber, Block BN, Poorbi Shalimar Bag , New Delhi, Delhi, 110088 Phone no.08826992243 \n7: Chemist Name:Jan Seva Chemist \nAddress:Shop Number 7, DDA market, near Remal Public School, Pocket 19, Sector 3, Rohini, New Delhi, Delhi, 110085 \nPhone no.081780 02252 \n8: Chemist Name:Soin Medical Store \nAddress:Shop Number 11 & 16, Sector 17A, Sector 17, Gurugram, Haryana 122001 \nPhone no.098990 03230 \n8 Chemist Nmae:Raj Chemist \nAddress:Shop No.5, Dda Market, AC-1, Shalimar, Shalimar Bagh, New Delhi, Delhi 110088 \nPhone no.092122 02369 \n9: Chemist Name:Shree Ram Medical Store \nAddress:29-A, Shalimar Bagh, Sahipur Village, Shalimar Bagh, Delhi 110088 \nPhone no.099995 74113 \n10: Chemist Name:Shri Shyam Ji Pharmacy \nAddress:U 16/55 , GROUND FLOOR, 122002, near METRO STATION, DLF Phase 3, Gurugram, Haryana 122002 \nPhone no.095605 37879 \n11: Chemist Name:Neelkanth Chemist \nAddress:shop no-G20 parsvnath plaza plot no- G-75 B, Sector 27, Noida, Uttar Pradesh 201301 \nPhone no.096543 50635 \n12: Chemist Name:Neha Medical Store \nAddress:Opposite D-17, P.R. Complex, Naya Bans, Sector 15, near Raj Hospital, Noida, Uttar Pradesh 201301 \nPhone no.096438 42701 \n13: Chemist Name:Sanjivani Pharmacy \nAddress:SHOP NO.16, A323A, A Block, Sector 19, Noida, Uttar Pradesh 201301 \nPhone no.070049 46827 \n14: Chemist Name:Govind Medical Store \nAddress:Shop no 1 Sohan Market,, Sector-5, Narela, Noida, Uttar Pradesh 201301 \nPhone No.075328 17400',['all chamist number','all chemist','numbers of chemist','chemist' ] , all_chemist_no=False)



    # WOMEN SCHEMES

    response('\n1:Schemes Name:Beti Bachao, Beti Padhao (BBBP) \n2:Schemes Name:Mahila e-Haat \n3:Schemes Name:Pradhan Mantri Matru Vandana Yojana (PMMVY) \n4:Schemes Name:Ujjawala Scheme \n5:Schemes Name:Mahila Shakti Kendra (MSK) \n6:Schemes Name:	National Mission for Empowerment of Women (NMEW) \n7:Schemes Name:Working Women Hostels \n8:Schemes Name:Swadhar Greh Scheme \n9:Schemes Name:Support to Training and Employment Programme for Women (STEP) \n10:Schemes Name:National Scheme for Incentive for the Girl Child for Secondary Education \n11:Schemes Name:One Stop Centre Scheme (OSC) \n12:Schemes Name:Rajiv Gandhi National Creche Scheme \n13:Schemes Name:National Rural Livelihoods Mission (NRLM) \n14:Schemes Name:National Scheme of Incentives to Girls for Secondary Education \n15:Schemes Name:Sukanya Samriddhi Yoj \n16:Schemes Name:Skill Development Initiatives \n17:Schemes Name:Indira Gandhi Matritva Sahyog Yojana (IGMSY) \n18:Schemes  Name:National Policy for Women \n19:Schemes Name:Gender Budgeting \n20:Schemes Name:National Rural Employment Guarantee Act (NREGA)',['women','women schemes','government schemes for women','women safety' ] , women_schemes=False)



    # women helpline number

    response('\n1: Women In Distress \nHelpline No. 1091 \n2: Women Helpline Domestic Abuse \nHelpline No. 181 \n3: Police \nHelpline No. 100 \n4: National Commison For Women (NCW) \nHelpline No. 7827170170  \n5: Delhi Commision For Women \nHelpline No. 011-23378044 \n6: Outer Delhi Helpline \nHelpline No. 011-27034873 \n7: Child Helpline \nHelpline No. 1098 \n8: National Human Right Commision \nHelpline No. 011-23385368 \n9: Delhi Commison for women \nHelpline No. 011-23379181 \n10: Delhi Women Protection Cell \nHelpline No. 011-24673366 \n11: Shakti Shalini ( N.G.O ) Women Shelter \nHelpline No. 011-24373737 \n12: Sakshi - violence intervention center \nHelpline No. (0124) 2562336 \n13: Uttar Pradesh Women commission \nHelpline No. 0522-2306403 \n14: Uttar Pradesh Women Helpline \nHelpline No. 1090 ',['women','helpline','women helpline number','women help' ] , women_helpline=False)





    # GN chemist stores

    response('\n1: Name: Navin Medical Store \nAddress: F-X43, 1st St, Pocket F, Block F, Sector Alpha II, Greater Noida, Brahmpur Rajraula Urf Nawada, Uttar Pradesh 201308 \nPhone No. 098715 45424 \n2: Name: Max 24 pharmacy \nAddress: Shop no 1&2, NH-29, Sector P-4, Block A, Phi III, Greater Noida, Uttar Pradesh 201310 \nPhone No. 088101 01066 \n3: Name: SHIV MEDICAL STORE \nAddress: Pal market, near govt school, Accher, Vill, Greater Noida, Uttar Pradesh 201310 \nPhone No. 088821 01808 \n4: Name: Apollo Pharmacy Sector Alpha I \nAddress: Shop No 36, Plot No C2, GF, Bibhag Plaza, Sector, Alpha-I Commercial Belt, Block E, Alpha I, Noida, Greater Noida, Uttar Pradesh 201301 \nPhone No. 088269 09795 \n5: Name: Medical Store \nAddress: shopping complex P3 Market, Phi III, Greater Noida, Uttar Pradesh 201310 \nPhone No. 095405 83626 \n6: Name: Dayal Medical Store \nAddress: Shop no. GF- 16 , Designarch Society, Site C Rd, Zeta II, Greater Noida, Uttar Pradesh 201306 \nPhone No. 089298 78521 \n7: Name: Shiv Medical Store \nAddress: NCR Region, 19, Greater Noida, Alpha I, Greater Noida, Uttar Pradesh 201306 \nPhone No. 093102 93012 \n8: Name: ITS Chemist Shop \nAddress: 47, Knowledge Park III, Greater Noida, Uttar Pradesh 201310 \nPhone No. 078400 01425 \n9: Name: J. S. B. Medical Stores \nAddress: , Greater Noida, Delhi NCR, Uttar Pradesh 201310 \nPhone No. 094112 29843 \n10: Name: Dev Medical Store \nAddress: Jalpura, Bisrakh Road, Greater Noida, Gautam Budh Nagar, Uttar Pradesh 201306 \nPhone No. 098718 83985',['chemist shop in greater noida','chemist greater noida','chemist greater'  ] , ch_greater=False)

    # delhi chemist shops 

    response('\n1: Name: Apollo Pharmacy Dwarka, Sector 10 \nAddress: Plot No 19, Manish Royal Plaza, SN G3, Sector 10 Dwarka, Dwarka, New Delhi, Delhi 110075 \nPhone No. 011 4308 9564 \n2: Name: Goyal Medical Store \nAddress: D-10, 27, Shiva Rd, Pocket 10, Sector 8D, Rohini, Delhi, 110085 \nPhone No. 092125 75133 \n3: Name: Medical Plaza \nAddress: Shop No. G-3, Plot No. 16, Central Market, Mall Rd, Pocket 1, Sector 10 Dwarka, Dwarka, New Delhi, Delhi 110075 \nPhone No. 099995 66192 \n4: Name: A S Medicos \nAddress: 24, Ram Nagar Market, Near New Delhi Railway Station, Pahar Ganj, New Delhi, Delhi 110055 \nPhone No. 088104 35072 \n5: Name: Dayal Pharmacy Store \nAddress: A-40/1, Mahendru Enclave, Gtk Road, A1, Gate Karnal Road, Division, Gujranwala Town, New Delhi, Delhi 110052 \nPhone No. 088103 18511 \n6: Name: Verma Medical Store \nAddress: Shop No. T-10, Azadpur, Azadpur, New Delhi, Delhi 110033 \nPhone No. 088822 38423 \n7: Name: The Chemist Shop \nAddress: A-305 GROUND FLOOR ,VIJAY VIHAR PH-, Rohini 110085, Rohini Sector 4 And 5 Dividing Road, New Delhi, Delhi 110085 \nPhone No. 070656 15880 \n8: Name: Heera Medical Store \nAddress: Shop No.1, C-5, Rana Pratap Bagh, Ashok Vihar, New Delhi, Delhi, 110007 \nPhone No. 075031 98483 \n9: Name: Pharmacy Medical Store \nAddress: 618f, 5, near Ambedkar Park, Vishwas Nagar, Shahdara, New Delhi, Delhi, 110032 \nPhone No. 096674 76226 \n10: Name: Narula Medical Store \nAddress: Postcode: 110009, F-14/32, Model Town Phase 2, Model Town, Delhi \nPhone No. 098910 23585',['delhi chemist','delhi chemist store','delhi shops' ] , d_chemmist=False)

    response('\n1: Name: Centralized Accident & Trauma Services (CATS) \nAddress: Near Gate No. 5, AIIMS, Ansari Nagar East, New Delhi, Delhi 110029 \nPhone No. 1099 \n2: Name: Delhi Ambulance Service \nAddress: F-13, Connaught Place, New Delhi, Delhi 110001 \nPhone No. 102 \n3: Name: Rapid Action Ambulance Service \nAddress: 32, Basant Lane, Gole Market, New Delhi, Delhi 110001 \nPhone No. 9871601333 \n4: Name: Life Care Ambulance Service \nAddress: 96-B, 3rd Floor, Adhchini, Sri Aurobindo Marg, New Delhi, Delhi 110017 \nPhone No.9873411116 \n5: Name: St. John Ambulance \nAddress: 2, Red Cross Road, New Delhi, Delhi 110001 \nPhone No. 011-23718181',['delhi ambulance','ambulances','delhi area ammbulance services' ] , d_amb=False)

    response('\n1: Name: Samvedna Ambulance Service \nAddress: 33, Aashirwad Enclave, Phase II, Khargapur, Civil Lines, Bareilly, Uttar Pradesh 243001 \nPhone: 9415094865,\n Name: SOS Ambulance Service \n Address: Near Basant Cinema, Badaun, Uttar Pradesh 243601 \n Phone: 9415022093, \n Name: Life Care Ambulance Service \n Address: Kursi Road, Near Patrakarpuram, Gomti Nagar, Lucknow, Uttar Pradesh 226010 \n Phnoe: 9415001802 , \n Name: Helping Hand Ambulance Service \n Address: Shop No. 15, Patel Nagar, Near Sant Nirankari Bhawan, Meerut, Uttar Pradesh 250001 \n Phone: 9839884155, \n St. John Ambulance	\n Address: 5/90, Vishal Khand, Gomti Nagar, Lucknow, Uttar Pradesh 226010	Phone: 9454947070',['uttar pradesh ambulances ', 'uttar pradesh', 'uttar presdesh area ambulances'], up_amb=False)

    response(long.R_EATING, ['What', 'you', 'eat'], required_words=['you','eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get) 
    #print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match



def get_response (user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response
# Testing the response system
while True:
    print('Bot: ' + get_response (input('You: ')))

    