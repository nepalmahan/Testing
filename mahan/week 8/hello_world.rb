# hello_world_spec.rb
require './hello_world'

RSpec.describe "Hello World" do
  it "returns Hello, World!" do
    expect(hello_world).to eq("Hello, World!")
  end
end
