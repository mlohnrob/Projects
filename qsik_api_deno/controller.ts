import { Party } from "./party_interface.ts";

// import { parties } from "./data.ts";

let parties: Array<Party> = [
  {
    id: "esddfw",
    owner: "August",
    name: "Augusts PArty",
    maxPeople: 15,
    people: ["9usreiopgue9p0g", "joaeofiaef"],
  },
  {
    id: "aefegf",
    owner: "erahqah",
    name: "aerhqh PArty",
    maxPeople: 15,
    people: ["rhaedhraehgg", "joayukdeofiaef"],
  },
  {
    id: "aretj",
    owner: "artdehrhr",
    name: "u,m PArty",
    maxPeople: 15,
    people: ["dtfykje", "detykked"],
  },
  {
    id: "sfrthj",
    owner: "dfyjyjd",
    name: "dyjyd PArty",
    maxPeople: 15,
    people: ["9usreiopgue9p0g", "joaeofiaef"],
  },
  {
    id: "esddfw",
    owner: "August",
    name: "Augusts PArty",
    maxPeople: 15,
    people: ["9usreiopgue9p0g", "joaeofiaef"],
  },
];

const home = async ({ response }: { response: any }) => {
  response.body = "Hello World!";
};

const getParties = async ({ response }: { response: any }) => {
  response.body = {
    success: true,
    data: parties,
  };
};

const getParty = async (
  { params, response }: { params: { id: string }; response: any },
) => {
  const party: Party | undefined = parties.find((party) =>
    party.id === params.id
  );

  if (party) {
    response.status = 200;
    response.body = {
      success: true,
      data: party,
    };
  } else {
    response.status = 404;
    response.body = {
      success: false,
      data: "Party not found",
    };
  }
};

const createParty = async (context: any) => {
  const body = await context.request.body(true);
  const party: Party = body.value;
  parties.push(
    {
      id: party.id,
      owner: party.owner,
      name: party.name,
      maxPeople: party.maxPeople,
      people: party.people,
    },
  );
  context.response.status = 201;
  context.response.body = {
    success: true,
    data: party,
  };
};

export { home, getParties, getParty, createParty };
