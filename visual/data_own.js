var nodes = [
    { id: "cancer", group: 0, label: "Cancer", level: 1 },
    { id: "diabetes", group: 0, label: "Diabetes", level: 1 },


    { id: "drug_1"   , group: 1, label: "Drug 1"   , level: 2 },
    { id: "drug_2"   , group: 1, label: "Drug 2"   , level: 2 },
    { id: "drug_3"   , group: 1, label: "Drug 3"   , level: 2 }

]


var links = [
    { target: "cancer", source: "drug_1" , strength: 0.1 },
    { target: "cancer", source: "drug_2" , strength: 0.7 },
    { target: "cancer", source: "drug_3" , strength: 0.2 },
    { target: "diabetes", source: "drug_1" , strength: 0.3 },
    { target: "diabetes", source: "drug_2" , strength: 0.7 }

]